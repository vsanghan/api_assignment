
def crypto_currency_converter(crypto, currency):
	# BTC = Bitcoin, ETH = Ethereum
	if crypto == 'Bitcoin':
		crypto_id = 'BTC'
	if crypto == 'Ethereum':
		crypto_id = 'ETH'

	key = '<Enter_your_key_here>'
	url = "https://api.nomics.com/v1/currencies/ticker?key="+key+"&ids="+crypto_id+"&interval=1h&convert="+currency
	j_response = json.loads(requests.get(url).text)
	# j_response = json.loads(response.text)
	
	if currency == 'INR':
		symbol = 'Rs.'
	elif currency == 'USD':
		symbol = '$'
	else:
		symbol = ''

	
	return "The {} coversion to {} is ".format(crypto, currency)+ symbol +str(j_response[0]['price'])

print (crypto_currency_converter('Ethereum','USD'))
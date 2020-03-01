def get_current_temperatur(city):
	key = '<Enter_your_key_here>'
	url = 'https://api.weatherbit.io/v2.0/current?city='+city+'&key='+key
	# print (url)
	response = requests.get(url) # sending a GET request to the URL
	# print(response, response.text, type(response.text))
	j_response = json.loads(response.text)
	# print(j_response, type(j_response))
	current_temp = j_response['data'][0]['temp']
	return (current_temp)

print(get_current_temperatur('Mumbai'))
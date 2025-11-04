from requests import get

currencies = get("https://www.cbr-xml-daily.ru/daily_json.js")

def get_currencies(codes = {}):
	data = currencies.json()

	if 'Valute' not in data:
		return None
	
	valutes = data['Valute']
	result = {}

	for code in codes:
		if code not in valutes:
			return None
		
		currency_data = valutes[code]
		result[code] = currency_data['Value']

	return result


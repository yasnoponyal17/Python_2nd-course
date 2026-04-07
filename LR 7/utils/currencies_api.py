import requests

def get_currencies(currency_codes=None, url="https://www.cbr-xml-daily.ru/daily_json.js"):
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        
        if 'Valute' not in data:
            return None
        
        valutes = data['Valute']
        result = {}

        if currency_codes is None:
            for code, info in valutes.items():
                result[code] = {
                    'id': info['ID'],
                    'num_code': info['NumCode'],
                    'char_code': info['CharCode'],
                    'name': info['Name'],
                    'value': info['Value'],
                    'nominal': info['Nominal']
                }
            return result

        for code in currency_codes:
            if code in valutes:
                info = valutes[code]
                result[code] = {
                    'id': info['ID'],
                    'num_code': info['NumCode'],
                    'char_code': info['CharCode'],
                    'name': info['Name'],
                    'value': info['Value'],
                    'nominal': info['Nominal']
                }

        return result
        
    except requests.exceptions.RequestException:
        return None
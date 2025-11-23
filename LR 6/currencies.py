import requests

def get_currencies(currency_codes, url="https://www.cbr-xml-daily.ru/daily_json.js"):
    try:
        response = requests.get(url)
        response.raise_for_status()
        
        data = response.json()
   
        if 'Valute' not in data:
            return None
        
        valutes = data['Valute']
        result = {}
        
        for code in currency_codes:
            if code in valutes:
                result[code] = valutes[code]['Value']
        
        return result
        
    except requests.exceptions.RequestException:
        return None
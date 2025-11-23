import requests
import sys

def get_currencies(currency_codes: list, url:str = "https://www.cbr-xml-daily.ru/daily_json.js", handle=sys.stdout)->dict:

    try:
        response = requests.get(url)
        response.raise_for_status() 
        data = response.json()
        currencies = {}

        if "Valute" in data:
            for code in currency_codes:
                if code in data["Valute"]:
                    currencies[code] = data["Valute"][code]["Value"]
                else:
                    handle.write(f"Код валюты '{code}' не найден.\n")
        return currencies

    except Exception as e:
        handle.write(f"Ошибка при выполнении запроса: {e}\n")
        return None

currency_list = ['USD', 'EUR', 'BYN', 'KEK']
    
result1 = get_currencies(currency_list)
print("Результат:", result1)
    
result2 = get_currencies(currency_list, url='https://скама.нет/daily_json.js')
print("Результат:", result2)
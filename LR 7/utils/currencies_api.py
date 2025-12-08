import requests

def get_currencies(url="https://www.cbr-xml-daily.ru/daily_json.js"):
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        if "Valute" not in data:
            return []

        result = []

        for code, valute in data["Valute"].items():
            result.append({
                "id": valute["ID"],
                "num_code": int(valute["NumCode"]),
                "char_code": valute["CharCode"],
                "name": valute["Name"],
                "value": float(valute["Value"]),
                "nominal": int(valute["Nominal"]),
            })

        return result

    except requests.exceptions.RequestException:
        return []

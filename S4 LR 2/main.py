from abc import ABC, abstractmethod
import json
import yaml

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


class Component(ABC):
    @abstractmethod
    def operation(self):
        pass

    @abstractmethod
    def save(self, filename: str):
        pass


class ConcreteComponent(Component):
    def __init__(self, codes):
        self.codes = codes

    def operation(self) -> dict:
        return get_currencies(self.codes)

    def save(self, filename: str):
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(str(self.operation()))

class Decorator(Component):
    
    def __init__(self, component: Component):
        self._component = component

    def operation(self):
        return self._component.operation()

    def save(self, filename: str):
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(self.operation())


class JsonDecorator(Decorator):
    def operation(self) -> str:
        result = self._component.operation()
        return json.dumps(result, indent=0)

class YamlDecorator(Decorator):
    def operation(self) -> str:
        result = self._component.operation()
        return yaml.dump(result, allow_unicode=True)

class CsvDecorator(Decorator):
    def operation(self) -> str:
        result = self._component.operation()
        lines = ["Currency,Value"]
        lines.extend([f"{code},{value}" for code, value in result.items()])
        return "\n".join(lines)


if __name__ == "__main__":
    codes = ['USD', 'EUR', 'BYN', 'UAH']
    
    source = ConcreteComponent(codes)
    
    json_result = JsonDecorator(source)
    json_result.save("currencies.json")

    yaml_result = YamlDecorator(source)
    yaml_result.save("currencies.yaml")

    csv_result = CsvDecorator(source)
    csv_result.save("currencies.csv")

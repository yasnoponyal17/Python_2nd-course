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


class ConcreteComponent(Component):
    def __init__(self, codes):
        self.codes = codes

    def operation(self) -> dict:
        return get_currencies(self.codes)


class Decorator(Component):
   
    _component: Component = None 

    def __init__(self, component: Component) -> None:
        self._component = component

    @property
    def component(self) -> Component:
        return self._component

    def operation(self):
        return self._component.operation()
    
class JsonDecorator(Decorator):
    def operation(self) -> str:
        result = self.component.operation()
        return json.dumps(result, indent=0)

class YamlDecorator(Decorator):
    def operation(self) -> str:
        result = self.component.operation()
        return yaml.dump(result, allow_unicode=True)
    
class CsvDecorator(Decorator):
    def operation(self) -> str:
        result = self.component.operation()
        
        lines = ["Currency,Value"]
        
        lines.extend([f"{code},{value}" for code, value in result.items()])
        
        return "\n".join(lines)
    

# Сохранение данных в файлы🤯🤯🤯
def save_to_file(component: Component, filename: str):
    result = component.operation()
    
    if not isinstance(result, str):
        content = str(result)
    else:
        content = result
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    

if __name__ == "__main__":
    codes = ['USD', 'EUR', 'BYN', 'UAH']
    source = ConcreteComponent(codes)

    json_result = JsonDecorator(source)
    save_to_file(json_result, "currencies.json")

    yaml_result = YamlDecorator(source)
    save_to_file(yaml_result, "currencies.yaml")

    csv_result = CsvDecorator(source)
    save_to_file(csv_result, "currencies.csv")

# Лабораторная работа 2. Шаблон "Декоратор"
## Постановка задачи
Написать фрагмент программы, которая использует шаблон (паттерн) «Декоратор». В качестве бизнес-логики реализовать базовый способ получения курсов валют в формате json (использовать материалы ЛР 6 из 3 семестра) с помощью API Центробанка. И реализовать конкретные декораторы, которые будут позволять преобразовывать результаты базового декоратора в Yaml-формат (библиотека PyYaml, нужно установить) и в CSV-формат (библиотека) csv (встроенная библиотека). Классы декораторы должны иметь помимо основного метода, который возвращает объект в соответствующем формате, метод, который сохраняет данные в файл соответствующего типа.

Пожалуйста, реализуйте наиболее правильным образом интерфейс (с использованием ABC и @abstractmethod).

## Код программы
```python
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

```
## Результат
### currencies.json
![json](./images/json.png)
### currencies.yaml
![yaml](./images/yaml.png)
### currencies.csv
![csv](./images/csv.png)

## Тестирование
```python
import unittest
import json
import yaml
from main import Component, JsonDecorator, YamlDecorator, CsvDecorator


class MockComponent(Component):
    def operation(self) -> dict:
        return {"USD": 666.0}

    def save(self, filename: str):
        pass

class TestCurrencyDecorators(unittest.TestCase):

    def setUp(self):
        """Этот метод запускается перед каждым тестом"""
        self.source = MockComponent()

    def test_json_decorator(self):
        decorator = JsonDecorator(self.source)
        result = decorator.operation()
        
        data = json.loads(result)
        self.assertEqual(data["USD"], 666.0)
        self.assertIn("USD", data)

    def test_yaml_decorator(self):
        decorator = YamlDecorator(self.source)
        result = decorator.operation()
        
        data = yaml.safe_load(result)
        self.assertEqual(data["USD"], 666.0)

    def test_csv_decorator(self):
        decorator = CsvDecorator(self.source)
        result = decorator.operation()
        
        self.assertIn("Currency,Value", result)
        self.assertIn("USD,666.0", result)


if __name__ == "__main__":
    unittest.main(verbosity=2)
```

### Ефимов Сергей Робертович, 2 курс, ИВТ-2
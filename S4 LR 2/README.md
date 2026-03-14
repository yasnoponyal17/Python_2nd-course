# Лабораторная работа 2. Шаблон "Декоратор"
В разработке...
## Постановка задачи
На основе кода ниже (main.py) написать фрагмент программы, которая использует шаблон (паттерн) «Декоратор». В качестве бизнес-логики реализовать базовый способ получения курсов валют в формате json (использовать материалы ЛР 6 из 3 семестра) с помощью API Центробанка. И реализовать конкретные декораторы, которые будут позволять преобразовывать результаты базового декоратора в Yaml-формат (библиотека PyYaml, нужно установить) и в CSV-формат (библиотека) csv (встроенная библиотека). Классы декораторы должны иметь помимо основного метода, который возвращает объект в соответствующем формате, метод, который сохраняет данные в файл соответствующего типа.

Пожалуйста, реализуйте наиболее правильным образом интерфейс (с использованием ABC и @abstractmethod).

```python
class Component():
    """
    Базовый интерфейс Компонента определяет поведение, которое изменяется
    декораторами.
    """

    def operation(self) -> str:
        pass


class ConcreteComponent(Component):
    """
    Конкретные Компоненты предоставляют реализации поведения по умолчанию. Может
    быть несколько вариаций этих классов.

    Для нашей программы ConcreteComponent - Класс возвращающий dict
    """

    def operation(self) -> str:
        return "ConcreteComponent"


class Decorator(Component):
    """
    Базовый класс Декоратора следует тому же интерфейсу, что и другие
    компоненты. Основная цель этого класса - определить интерфейс обёртки для
    всех конкретных декораторов. Реализация кода обёртки по умолчанию может
    включать в себя поле для хранения завёрнутого компонента и средства его
    инициализации.
    """

    _component: Component = None

    def __init__(self, component: Component) -> None:
        self._component = component

    @property
    def component(self) -> str:
        """
        Декоратор делегирует всю работу обёрнутому компоненту.
        """

        return self._component

    def operation(self) -> str:
        return self._component.operation()


class ConcreteDecoratorA(Decorator):
    """
    Конкретные Декораторы вызывают обёрнутый объект и изменяют его результат
    некоторым образом.

    Для нашей программы ConcreteDecoratorA - Класс возвращающий json
    """

    def operation(self) -> str:
        """
        Декораторы могут вызывать родительскую реализацию операции, вместо того,
        чтобы вызвать обёрнутый объект напрямую. Такой подход упрощает
        расширение классов декораторов.
        """
        return f"ConcreteDecoratorA({self.component.operation()})"


class ConcreteDecoratorB(Decorator):
    """
    Декораторы могут выполнять своё поведение до или после вызова обёрнутого
    объекта.

    Для нашей программы ConcreteDecoratorA - Класс возвращающий csv

    """

    def operation(self) -> str:
        return f"ConcreteDecoratorB({self.component.operation()})"


def client_code(component: Component) -> None:
    """
    Клиентский код работает со всеми объектами, используя интерфейс Компонента.
    Таким образом, он остаётся независимым от конкретных классов компонентов, с
    которыми работает.
    """

    # ...

    print(f"RESULT: {component.operation()}", end="")

    # ...
```

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
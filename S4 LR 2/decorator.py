import json
import csv
import yaml
import requests
from abc import ABC, abstractmethod
from typing import Dict, Any, List

class Component(ABC):
    """
    Базовый интерфейс Компонента определяет поведение, 
    которое может быть изменено декораторами.
    """

    @abstractmethod
    def operation(self) -> Any:
        """Возвращает данные о курсах валют."""
        pass

# --- Конкретный компонент ---

class CurrenciesComponent(Component):
    """
    Конкретный Компонент предоставляет реализацию получения данных.
    Возвращает dict с курсами валют от ЦБ РФ.
    """

    def __init__(self, currency_codes: List[str]) -> None:
        self._currency_codes = currency_codes
        self._url = "https://www.cbr-xml-daily.ru/daily_json.js"

    def operation(self) -> Dict[str, float]:
        """
        Получает курсы валют в формате словаря.
        
        :return: Словарь вида {'USD': 75.0, ...} или пустой словарь при ошибке.
        """
        try:
            response = requests.get(self._url, timeout=10)
            response.raise_for_status()
            data = response.json()
            
            valutes = data.get('Valute', {})
            return {code: valutes[code]['Value'] for code in self._currency_codes if code in valutes}
        except (requests.RequestException, KeyError):
            return {}

class Decorator(Component):
    """
    Базовый класс Декоратора следует тому же интерфейсу, что и компонент.
    """

    def __init__(self, component: Component) -> None:
        self._component = component

    @property
    def component(self) -> Component:
        """Ссылка на обернутый компонент."""
        return self._component

    def operation(self) -> Any:
        """Делегирование операции обернутому компоненту."""
        return self._component.operation()


class JsonDecorator(Decorator):
    """Декоратор для преобразования данных в JSON и сохранения в файл."""

    def operation(self) -> str:
        """Возвращает строку в формате JSON."""
        return json.dumps(self.component.operation(), indent=4)

    def save_to_file(self, filename: str) -> None:
        """Сохраняет JSON данные в файл."""
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(self.operation())

class YamlDecorator(Decorator):
    """Декоратор для преобразования данных в YAML и сохранения в файл."""

    def operation(self) -> str:
        """Возвращает строку в формате YAML."""
        return yaml.dump(self.component.operation(), allow_unicode=True)

    def save_to_file(self, filename: str) -> None:
        """Сохраняет YAML данные в файл."""
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(self.operation())

class CsvDecorator(Decorator):
    """Декоратор для преобразования данных в CSV и сохранения в файл."""

    def operation(self) -> str:
        """Возвращает строку в формате CSV."""
        data = self.component.operation()
        output = "Currency,Value\n"
        for code, value in data.items():
            output += f"{code},{value}\n"
        return output

    def save_to_file(self, filename: str) -> None:
        """Сохраняет данные в CSV файл с использованием библиотеки csv."""
        data = self.component.operation()
        with open(filename, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['Currency', 'Value'])
            for item in data.items():
                writer.writerow(item)

# --- Клиентский код ---

if __name__ == "__main__":
    codes = ["USD", "EUR", "CNY"]
    base_service = CurrenciesComponent(codes)

    print("--- Базовый компонент (Dict) ---")
    print(base_service.operation())

    print("\n--- JSON Декоратор ---")
    json_service = JsonDecorator(base_service)
    print(json_service.operation())
    json_service.save_to_file("rates.json")

    print("\n--- YAML Декоратор ---")
    yaml_service = YamlDecorator(base_service)
    print(yaml_service.operation())
    yaml_service.save_to_file("rates.yaml")

    print("\n--- CSV Декоратор ---")
    csv_service = CsvDecorator(base_service)
    print(csv_service.operation())
    csv_service.save_to_file("rates.csv")
from abc import ABC, abstractmethod
from typing import Dict, List, Optional

import requests
import json
import yaml
import io
import csv


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


class Component():
    """
    Базовый интерфейс Компонента определяет поведение, которое изменяется
    декораторами.
    """

    def operation(self) -> object:
        pass
    
    
class CurrencySource(Component):
    """Конкретный компонент: запрашивает курсы валют и возвращает ``dict``.

    Args:
        currency_codes: Список ISO-кодов валют для запроса.
        url: URL API Центробанка (можно переопределить в тестах).
    """

    def __init__(
        self,
        currency_codes: List[str],
        url: str = "https://www.cbr-xml-daily.ru/daily_json.js",
    ) -> None:
        """Инициализировать источник данных."""
        self._currency_codes = currency_codes
        self._url = url

    def operation(self) -> Optional[Dict[str, float]]:
        """Вернуть словарь ``{код: курс}`` или ``None``.

        Returns:
            Словарь с курсами валют или ``None`` при ошибке.
        """
        return get_currencies(self._currency_codes, self._url)


class CurrencyDecorator(Component, ABC):
    """Абстрактный базовый декоратор.

    Хранит ссылку на обёрнутый компонент и делегирует ему вызов ``operation``.
    Подклассы обязаны реализовать ``operation`` и ``save_to_file``.
    """

    def __init__(self, component: Component) -> None:
        """Инициализировать декоратор с обёрнутым компонентом.

        Args:
            component: Компонент, чей результат будет преобразован.
        """
        self._component = component

    @property
    def component(self) -> Component:
        """Вернуть обёрнутый компонент."""
        return self._component

    @abstractmethod
    def operation(self) -> object:
        """Преобразовать результат обёрнутого компонента."""

    @abstractmethod
    def save_to_file(self, filepath: str) -> None:
        """Сохранить результат ``operation`` в файл.

        Args:
            filepath: Путь к создаваемому файлу.
        """

class JsonDecorator(CurrencyDecorator):
    """Декоратор, преобразующий результат компонента в JSON-строку.

    Принимает ``dict`` от обёрнутого компонента и сериализует его в
    красиво отформатированный JSON (``indent=2``, ``ensure_ascii=False``).
    """

    def operation(self) -> Optional[str]:
        """Вернуть курсы валют в виде JSON-строки.

        Returns:
            JSON-строка или ``None``, если базовый компонент вернул ``None``.
        """
        data = self._component.operation()
        if data is None:
            return None
        return json.dumps(data, indent=2, ensure_ascii=False)

    def save_to_file(self, filepath: str) -> None:
        """Сохранить JSON-представление курсов в файл ``.json``.

        Args:
            filepath: Путь к выходному файлу.

        Raises:
            ValueError: Если данные недоступны (компонент вернул ``None``).
        """
        result = self.operation()
        if result is None:
            raise ValueError("Нет данных для сохранения (API вернул None).")
        with open(filepath, "w", encoding="utf-8") as fh:
            fh.write(result)
            

class YamlDecorator(CurrencyDecorator):
    """Декоратор, преобразующий результат компонента в YAML-строку.

    Использует библиотеку ``PyYAML``.
    """

    def operation(self) -> Optional[str]:
        """Вернуть курсы валют в виде YAML-строки.

        Returns:
            YAML-строка или ``None``, если базовый компонент вернул ``None``.
        """
        data = self._component.operation()
        if data is None:
            return None
        return yaml.dump(data, allow_unicode=True, default_flow_style=False)

    def save_to_file(self, filepath: str) -> None:
        """Сохранить YAML-представление курсов в файл ``.yaml``.

        Args:
            filepath: Путь к выходному файлу.

        Raises:
            ValueError: Если данные недоступны.
        """
        result = self.operation()
        if result is None:
            raise ValueError("Нет данных для сохранения (API вернул None).")
        with open(filepath, "w", encoding="utf-8") as fh:
            fh.write(result)
            
class CsvDecorator(CurrencyDecorator):
    """Декоратор, преобразующий результат компонента в CSV-строку.

    Использует встроенную библиотеку ``csv``.
    Формат строк: ``currency_code,value``.
    """

    def operation(self) -> Optional[str]:
        """Вернуть курсы валют в виде CSV-строки.

        Первая строка — заголовок ``currency_code,value``.

        Returns:
            CSV-строка или ``None``, если базовый компонент вернул ``None``.
        """
        data = self._component.operation()
        if data is None:
            return None

        output = io.StringIO()
        writer = csv.writer(output)
        writer.writerow(["currency_code", "value"])
        for code, value in data.items():
            writer.writerow([code, value])
        return output.getvalue()

    def save_to_file(self, filepath: str) -> None:
        """Сохранить CSV-представление курсов в файл ``.csv``.

        Args:
            filepath: Путь к выходному файлу.

        Raises:
            ValueError: Если данные недоступны.
        """
        result = self.operation()
        if result is None:
            raise ValueError("Нет данных для сохранения (API вернул None).")
        with open(filepath, "w", encoding="utf-8", newline="") as fh:
            fh.write(result)
            
def client_code(component: Component) -> None:
    """Продемонстрировать работу компонента через его интерфейс.

    Args:
        component: Любой объект, реализующий ``Component``.
    """
    result = component.operation()
    print(f"RESULT:\n{result}\n")
    
    
    
if __name__ == "__main__":
    CODES = ["USD", "EUR", "BYN", "UAH"]

    source = CurrencySource(CODES)
    client_code(source)

    print("JSON")
    json_dec = JsonDecorator(source)
    client_code(json_dec)
    json_dec.save_to_file("currencies.json")

    print("YAML")
    yaml_dec = YamlDecorator(source)
    client_code(yaml_dec)
    yaml_dec.save_to_file("currencies.yaml")

    print("CSV")
    csv_dec = CsvDecorator(source)
    client_code(csv_dec)
    csv_dec.save_to_file("currencies.csv")


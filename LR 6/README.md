# Лабораторная работа 6. Курсы валют
Скоро...
## Постановка задачи
Написать функцию get_currencies(currency_codes, url), которая обращается к API по url (по умолчанию - https://www.cbr-xml-daily.ru/daily_json.js) и возвращает словарь курсов валют для валют из списка currency_codes.

В возвращаемом словаре ключи - символьные коды валют, а значения - их курсы.

В случае ошибки запроса функция должна вернуть None.

Для обращения к API использовать функцию get модуля requests.

Для установки requests можно использовать команду:
```bash
pip install requests
```
#### Итерация 1
Предусмотреть в функции логирование ошибок с использованием стандартного потока вывода (sys.stdout).

Функция должна обрабатывать следующие исключения:

- в ответе не содержатся курсы валют;
- в словаре курсов валют нет валюты из списка currency_codes;
- ошибка выполнения запроса к API.
#### Итерация 2
Вынести логирование ошибок из функции get_currencies(currency_codes, url) в декоратор.
#### Итерация 3
Оформить логирование ошибок с использованием модуля logging.
#### Тестирование должно содержать:
- проверку ключей и значений возвращаемого словаря;
- проверку обработки исключений;
- проверку записей логов в поток вывода.
## Код программы
### Чистая функция get_currencies
```python
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
```
### Итерация 1. Стандартный поток вывода
```python
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
```
### Итерация 2. Декоратор
```python
import sys
from functools import wraps
from currencies import get_currencies

def trace(handle=sys.stdout):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                handle.write(f"Ошибка в функции {func.__name__}: {e}\n")
                raise
        return wrapper
    return decorator

from currencies import get_currencies

@trace(handle=sys.stdout)
def get_currencies_trace(currency_codes, url):
    return get_currencies(currency_codes, url)
```
### Итерация 3. Модуль logging
```python
import logging
from currencies import get_currencies

logging.basicConfig(
    filename="currencies.log",
    level=logging.DEBUG,
    format="%(levelname)s: %(message)s"
)

logger = logging.getLogger("currency_api")

def get_currencies_logging(currency_codes, url="https://www.cbr-xml-daily.ru/daily_json.js"):
    logger.info(f"Codes: {currency_codes}")
    
    try:
        result = get_currencies(currency_codes, url)
        
        if result is None:
            logger.error("API returned invalid data or a request error occurred")
        else:
            not_found = [code for code in currency_codes if code not in result]
            for code in not_found:
                logger.warning(f"Code '{code}' was not found.")
            
            logger.info(f"Number of exchange rates received: {len(result)}")
        
        return result
        
    except Exception as e:
        logger.error(f"Error while executing request: {e}")
        return None
```
## Результат
### Итерация 1
![Результат](images/result-1.png)
### Итерация 2
![Результат](images/result-2.png)
### Итерация 3
![Результат](images/result-3.png)
## Пояснение к коду
## Тестирование
## Результат
### Ефимов Сергей Робертович, 2 курс, ИВТ-2
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

try:
    result1 = get_currencies_trace(['USD', 'EUR'])
    print("Результат:", result1)
except Exception as e:
    print("Исключение перехвачено:", e)
    
try:
    result2 = get_currencies_trace(['USD'], url='https://неверный-сайт.ru/daily_json.js')
    print("Результат:", result2)
except Exception as e:
    print("Исключение перехвачено:", e)
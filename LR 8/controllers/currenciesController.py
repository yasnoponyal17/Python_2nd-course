from jinja2 import Environment, FileSystemLoader, select_autoescape
from models.currency import Currency
from utils.currencies_api import get_currencies

env = Environment(
    loader=FileSystemLoader('templates'),
    autoescape=select_autoescape()
)

template_currencies = env.get_template("currencies.html")

def currencies():
    data = get_currencies()

    currencies_list = []

    if isinstance(data, dict):
        for curr in data.values():
            try:
                currencies_list.append(
                    Currency(
                        curr['id'],
                        curr['num_code'],
                        curr['char_code'],
                        curr['name'],
                        curr['value'],
                        curr['nominal']
                    )
                )
            except Exception:
                continue

    return template_currencies.render(currencies=currencies_list)
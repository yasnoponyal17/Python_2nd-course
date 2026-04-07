from jinja2 import Environment, FileSystemLoader, select_autoescape
from utils.currencies_api import get_currencies
from models.user import User
from models.currency import Currency
from models.usercurrency import UserCurrency

env = Environment(
    loader=FileSystemLoader('templates'),
    autoescape=select_autoescape()
)

template_users = env.get_template('users.html')
template_user = env.get_template('user.html')

users_info = [
	User(1, 'Кто-то'),
	User(2, 'Ещё кто-то')
]

user_currencies = [
    UserCurrency(1, 1, "USD"),
    UserCurrency(2, 1, "EUR"),
    UserCurrency(3, 2, "GBP"),
    UserCurrency(4, 2, "JPY"),
]

def users():
    return template_users.render(users=users_info)

def user(user_id):
    for u in users_info:
        if u.id == user_id:
            user = u
            break
        
    currency_codes = []
    
    for uc in user_currencies:
        if uc.user_id == user.id:
            currency_codes.append(uc.currency_id)
            
    currencies_list = []
    
    if currency_codes:
        currencies_data = get_currencies(currency_codes)

        for curr in currencies_data.values():
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

    return template_user.render(
        user=user,
        currencies=currencies_list
    )
    
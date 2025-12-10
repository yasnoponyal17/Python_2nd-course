from http.server import HTTPServer, BaseHTTPRequestHandler
from jinja2 import Environment, PackageLoader, select_autoescape
from urllib.parse import urlparse, parse_qs

import os
STATIC_DIR = os.path.join(os.path.dirname(__file__), "static")

from models import App, Author, User, Currency, UserCurrency
from utils.currencies_api import get_currencies

env = Environment(
    loader=PackageLoader("myapp"),
    autoescape=select_autoescape()
)

CURRENCY_NAME_FIX = {
    "Алжирских динаров": "Алжирский динар",
    "Армянских драмов": "Армянский драм",
    "Форинтов": "Форинт",
    "Донгов": "Донг",
    "Гонконгских долларов": "Гонконгский доллар",
    "Египетских фунтов": "Египетский фунт",
    "Индийских рупий": "Индийская рупия",
    "Рупий": "Рупия",
    "Иранских риалов": "Иранский риал",
    "Сомов": "Сом",
    "Кубинских песо": "Кубинский песо",
    "Молдавских леев": "Молдавский лей",
    "Тугриков": "Тугрик",
    "Найр": "Найра",
    "Норвежских крон": "Норвежская крона",
    "Батов": "Бат",
    "Так": "Така",
    "Турецких лир": "Турецкая лира",
    "Узбекских сумов": "Узбекский сум",
    "Гривен": "Гривна",
    "Чешских крон": "Чешская крона",
    "Шведских крон": "Шведская крона",
    "Эфиопских быров": "Эфиопский быр",
    "Сербских динаров": "Сербский динар",
    "Рэндов": "Рэнд",
    "Вон": "Вона",
    "Иен": "Иена",
    "Кьятов": "Кьят",
}

template_index = env.get_template("index.html")
template_users = env.get_template("users.html")
template_currencies = env.get_template("currencies.html")
template_author = env.get_template("author.html")
template_user = env.get_template("user.html")

app = App('Курсы валют', '1.0.0', Author('Ефимов Сергей Робертович', '2об_ИВТ-2'))

users = [
    User(1, "Ким Чен Ын"),
    User(2, "OG Buda"),
    User(3, "Субо братик"),
    User(4, "Папич")
]

currencies = [
    Currency("R01235", 840, "USD", "Доллар США", 0, 1),
    Currency("R01239", 978, "EUR", "Евро", 0, 1),
    Currency("R01815", 410, "KRW", "Вон", 0, 1000),
    Currency("RO1135", 348, "HUF", "Венгерских форинтов", 0, 100)
]

user_currencies = [
    UserCurrency(1, 1, "R01235"),
    UserCurrency(2, 1, "R01815"),
    UserCurrency(3, 2, "R01235"),
    UserCurrency(4, 2, "R01135"),
]

def get_user_by_id(uid: int):
    return next((u for u in users if u.id == uid), None)


def get_currency_by_id(cid: str):
    return next((c for c in currencies if c.id == cid), None)

def update_currency_rates():
        codes = [c.char_code for c in currencies]
        rates = get_currencies(codes)

        if not rates:
            return

        for c in currencies:
            if c.char_code in rates:
                c.value = rates[c.char_code]


def get_user_subscriptions(uid: int):
    return [
        get_currency_by_id(uc.currency_id)
        for uc in user_currencies
        if uc.user_id == uid
    ]

def load_all_currencies_from_api():
    global currencies

    api_data = get_currencies()
    currencies = []

    for c in api_data:
        name = c["name"]

        if name in CURRENCY_NAME_FIX:
            name = CURRENCY_NAME_FIX[name]

        currencies.append(
            Currency(
                c["id"],
                c["num_code"],
                c["char_code"],
                name, 
                c["value"],
                c["nominal"]
            )
        )


class HttpHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        parsed = urlparse(self.path)
        path = parsed.path
        params = parse_qs(parsed.query)

        if path.startswith("/static/"):
            file_path = os.path.join(STATIC_DIR, path.replace("/static/", ""))

            if not os.path.exists(file_path):
                return self.respond(404, "File not found")

            with open(file_path, "rb") as f:
                data = f.read()

            if file_path.endswith(".css"):
                self.send_response(200)
                self.send_header("Content-Type", "text/css")
                self.end_headers()
                self.wfile.write(data)
                return

        if path == "/":
            return self.index(params)

        if path == "/users":
            return self.users_page(params)

        if path == "/user":
            return self.user_page(params)

        if path == "/currencies":
            return self.currencies_page(params)

        if path == "/author":
            return self.author_page(params)

        return self.respond(404, "<h1>404 — Страница не найдена</h1>")

    def index(self, params):
        html = template_index.render(
            app = app,
        )
        return self.respond(200, html)

    def users_page(self, params):
        html = template_users.render(
            users=users,
            app = app,
        )
        return self.respond(200, html)

    def user_page(self, params):
        if "id" not in params:
            return self.respond(400, "<h1>Error: id is required</h1>")

        try:
            uid = int(params["id"][0])
        except:
            return self.respond(400, "<h1>Error: id must be integer</h1>")

        user = get_user_by_id(uid)
        if not user:
            return self.respond(404, "<h1>Пользователь не найден</h1>")

        subscriptions = get_user_subscriptions(uid)

        html = template_user.render(app = app, user = user, subscriptions = subscriptions)

        return self.respond(200, html)

    
    def currencies_page(self, params):
        load_all_currencies_from_api()
        html = template_currencies.render(app=app, currencies=currencies)
        return self.respond(200, html)



    def author_page(self, params):
        html = template_author.render(app = app)
        return self.respond(200, html)
    
    


    def respond(self, status, body):
        self.send_response(status)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(body.encode("utf-8"))


def start_server(host="127.0.0.1", port=8000):
    server = HTTPServer((host, port), HttpHandler)
    print(f"Сервер запущен: http://{host}:{port}")
    server.serve_forever()


if __name__ == "__main__":
    start_server()

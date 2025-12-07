from http.server import HTTPServer, BaseHTTPRequestHandler
from jinja2 import Environment, PackageLoader, select_autoescape
from urllib.parse import urlparse, parse_qs

from models import App, Author, User, Currency, UserCurrency

env = Environment(
    loader=PackageLoader("myapp"),
    autoescape=select_autoescape()
)

template_index = env.get_template("index.html")
template_users = env.get_template("users.html")
template_currencies = env.get_template("currencies.html")

app = App('Currency App', '1.0.0', Author('Ефимов Сергей Робертович', '2об_ИВТ-2'))

# author = Author("Ефимов Сергей Робертович", "2об_ИВТ-2")
# app_info = App("Currency App", "1.0.0", author)

users = [
    User(1, "Ким Чен Ын"),
    User(2, "OG Buda"),
]

currencies = [
    Currency("R01235", 840, "USD", "Доллар США", 93.45, 1),
    Currency("R01239", 978, "EUR", "Евро", 101.12, 1),
    Currency("R01280", 360, "IDR", "Рупий", 48.6178, 10000),
]

user_currencies = [
    UserCurrency(1, 1, "R01235"),
    UserCurrency(2, 1, "R01239"),
    UserCurrency(3, 2, "R01280"),
]

def get_user_by_id(uid: int):
    return next((u for u in users if u.id == uid), None)


def get_currency_by_id(cid: str):
    return next((c for c in currencies if c.id == cid), None)


def get_user_subscriptions(uid: int):
    return [
        get_currency_by_id(uc.currency_id)
        for uc in user_currencies
        if uc.user_id == uid
    ]

class HttpHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        parsed = urlparse(self.path)
        path = parsed.path
        params = parse_qs(parsed.query)

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
            users=users
        )
        return self.respond(200, html)

    def user_page(self, params):
        if "id" not in params:
            return self.respond(400, "<h1>Error: id is required</h1>")

        try:
            uid = int(params["id"][0])
        except:
            return self.respond(400, "<h1>Error: id must be integer</h1>")

        user_obj = get_user_by_id(uid)
        if not user_obj:
            return self.respond(404, "<h1>Пользователь не найден</h1>")

        subscriptions = get_user_subscriptions(uid)

        html = f"""
        <h1>{user_obj.name}</h1>
        <h2>Подписки:</h2>
        <ul>
        {''.join(f'<li>{c.char_code} — {c.name} — {c.value}</li>' for c in subscriptions)}
        </ul>
        """

        return self.respond(200, html)


    def currencies_page(self, params):
        html = template_currencies.render(
            currencies=currencies
        )
        return self.respond(200, html)


    def author_page(self, params):
        html = f"""
        <h1>Автор приложения</h1>
        <p>Имя: {app.author.name}</p>
        <p>Группа: {app.author.group}</p>
        """
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

from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs

from models import App, Author, User, Currency, UserCurrency

author = Author("Ефимов Сергей Робертович", "2об_ИВТ-2")
app_info = App("Currency App", "1.0.0", author)

users = [
    User(1, "Ким Чен Ын"),
    User(2, "OG Buda"),
    User(3, "Evelone192"),
    User(4, "Меллстрой"),
    User(5, "Усама бен Ладен")
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
    """
    Возвращает список валют, на которые подписан пользователь.
    """
    links = [uc for uc in user_currencies if uc.user_id == uid]
    return [get_currency_by_id(link.currency_id) for link in links]


class MyHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        parsed = urlparse(self.path)
        path = parsed.path
        params = parse_qs(parsed.query)

        if path == "/":
            self.respond(200, f"""
                <h1>{app_info.name}</h1>
                <p>Версия: {app_info.version}</p>
                <p>Автор: {app_info.author.name} ({app_info.author.group})</p>
                <p><a href='/users'>Пользователи</a></p>
                <p><a href='/currencies'>Валюты</a></p>
            """)
            return

        if path == "/author":
            a = app_info.author
            self.respond(200, f"""
                <h1>Автор</h1>
                <p><b>Имя:</b> {a.name}</p>
                <p><b>Группа:</b> {a.group}</p>
            """)
            return

        if path == "/users":
            html = "<h1>Список пользователей</h1><ul>"
            for u in users:
                html += f"<li>{u.id}: {u.name} — <a href='/user?id={u.id}'>подробнее</a></li>"
            html += "</ul>"
            self.respond(200, html)
            return


        if path == "/user":
            if "id" not in params:
                self.respond(400, "<h1>Error: id должен быть указан</h1>")
                return

            try:
                uid = int(params["id"][0])
            except:
                self.respond(400, "<h1>Error: id должен быть числом</h1>")
                return

            user = get_user_by_id(uid)
            if not user:
                self.respond(404, "<h1>Пользователь не найден</h1>")
                return

            subs = get_user_subscriptions(uid)

            html = f"<h1>Пользователь: {user.name}</h1>"
            html += "<h2>Подписки:</h2><ul>"
            for c in subs:
                html += f"<li>{c.char_code} — {c.name} — {c.value} (номинал {c.nominal})</li>"
            html += "</ul>"

            self.respond(200, html)
            return

        if path == "/currencies":
            html = "<h1>Валюты</h1><ul>"
            for c in currencies:
                html += f"<li>{c.char_code} — {c.name}: {c.value} за {c.nominal}</li>"
            html += "</ul>"
            self.respond(200, html)
            return

        self.respond(404, "<h1>404 — Страница не найдена</h1>")


    def respond(self, status: int, body: str):
        self.send_response(status)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(body.encode("utf-8"))


def start_server(host="127.0.0.1", port=8000):
    server = HTTPServer((host, port), MyHandler)
    print(f"Сервер запущен на http://{host}:{port}")
    server.serve_forever()


if __name__ == "__main__":
    start_server()

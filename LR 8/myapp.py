from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs

from models.author import Author
from models.app import App

from controllers.databaseController import DatabaseController
from controllers.currenciesController import CurrenciesController
from controllers.userController import UserController
from controllers import pages


author_info = Author('Сергей Ефимов', 'ИВТ-2')
app_info = App('Конвертер валют', '2.2.8', author_info)

db = DatabaseController()
currencies_ctrl = CurrenciesController(db)
user_ctrl = UserController(db)


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed_url = urlparse(self.path)
        path = parsed_url.path
        query = parse_qs(parsed_url.query)
        
        if path == '/':
            content = pages.render_index(author_info, app_info)
        elif path == '/author':
            content = pages.render_author(author_info)
        elif path == '/currencies':
            data = currencies_ctrl.list_currencies()
            content = pages.render_currencies(data)
        elif path == '/users':
            data = user_ctrl.list_users()
            content = pages.render_users(data)
        elif path == '/user':
            user_id = int(query['id'][0])
            current_user = user_ctrl.get_user(user_id)
            currencies = user_ctrl.get_user_currencies(user_id)
            content = pages.render_user(current_user, currencies)
        elif path == '/currency/delete':
            currency_id = int(query['id'][0])
            currencies_ctrl.delete_currency(currency_id)
            self.send_response(302)
            self.send_header('Location', '/currencies')
            self.end_headers()
            return
        elif path == '/currency/update':
            char_code = list(query.keys())[0]
            value = float(query[char_code][0])
            currencies_ctrl.update_currency(char_code, value)
            self.send_response(302)
            self.send_header('Location', '/currencies')
            self.end_headers()
            return
        elif path == '/currency/show':
            data = currencies_ctrl.list_currencies()
            for row in data:
                print(dict(row))
            self.send_response(302)
            self.send_header('Location', '/currencies')
            self.end_headers()
            return
        else:
            content = "<h1>404 - Страница не найдена</h1>"
        


        self.send_response(200)
        self.send_header('Content-Type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode("utf-8"))
        
                    
hostName = "localhost"
serverPort = 8000

server = HTTPServer((hostName, serverPort), Handler)
print(f"Сервер запущен: http://{hostName}:{serverPort}")

try:
    server.serve_forever()
except KeyboardInterrupt:
    pass
    
server.server_close()
print("Сервер остановлен")

from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs

from models.author import Author
from models.app import App

from controllers.authorController import index, author
from controllers.currenciesController import currencies
from controllers.userController import users, user


author_info = Author('Сергей Ефимов', 'ИВТ-2')
app = App('Конвертер валют', '2.2.8', author)


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed_url = urlparse(self.path)
        path = parsed_url.path
        query = parse_qs(parsed_url.query)
        
        if path == '/':
            content = index(author_info, app)
        elif path == '/author':
            content = author(author_info)
        elif path == '/currencies':
            content = currencies()
        elif path == '/users':
            content = users()
        elif path == '/user':
            user_id = int(query['id'][0])
            content = user(user_id)
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

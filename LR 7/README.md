# Лабораторная работа 7. Клиент-серверное приложение
В разработке...
## Цель работы

1. Создать простое клиент-серверное приложение на Python без серверных фреймворков.

2. Освоить работу с HTTPServer и маршрутизацию запросов.

3. Применять шаблонизатор Jinja2 для отображения данных.

4. Реализовать модели предметой области (User, Currency, UserCurrency, App, Author) с геттерами и сеттерами.

5. Структурировать код в соответствии с архитектурой MVC.

6. Получать данные о курсах валют через функцию get_currencies и отображать их пользователям.

7. Реализовать функциональность подписки пользователей на валюты и отображение динамики их изменения.

8. Научиться создавать тесты для моделей и серверной логики.

## Описание моделей
### Author
- name - имя автора
- group - учебная группа

Используется для отображения информации об авторе на главной странице.

### App
- name - название приложения
- version - версия приложения 
- author - объект Author

Описывает само приложение.

### User
- id - уникальный идентификатор
- name - имя пользователя

Описывает пользователя системы.

### Currency
- id - уникальный идентификатор
- num_code - цифровой код
- char_code - символьный код
- name - название валюты
- value - курс валюты
- nominal - номинал

Описывает валюту и её текущий курс.

### UserCurrency
- id - уникальный идентификатор
- user_id - внешний ключ к User
- currency_id - внешний ключ к Currency

Реализует связь между пользователями и валютами.

## Архитектура проекта
```text
myapp/
├── models/
│ ├── __init__.py
│ ├── author.py
│ ├── app.py
│ ├── user.py
│ ├── currency.py
│ └── user_currency.py
├── templates/
│ ├── 404.html
│ ├── author.html
│ └── currencies.html
│ └── index.html
│ └── user.html
│ └── users.html
├── static/
│ └── css, js, images
├── myapp.py
└── utils/
 └── currencies_api.py
```

## Описание реализации
### Модели и их свойства (геттеры/сеттеры)
### Маршруты и обработка запросов
Сервер реализован с использованием стандартных библиотек:
- HTTPServer
- BaseHTTPRequestHandler

Маршрутизация выполняется через анализ пути:
```python
parsed = urlparse(self.path)
path = parsed.path
params = parse_qs(parsed.query)
```

Поддерживаются следующие маршруты:
- / - главная страница
- /users - список пользователей
- /user?id=... - информация о конкретном пользователе
- /currencies - список валют с курсами
- /author - информация об авторе

Каждый маршрут обрабатывается отдельным методом:
- index()
- users_page()
- user_page()
- currencies_page()
- author_page()
### Шаблонизатор Jinja2
Инициализация окружения выполняется один раз при запуске приложения:
```python
env = Environment(
    loader=PackageLoader("myapp"),
    autoescape=select_autoescape()
)
```

Потом загружаются шаблоны:
```python
template_index = env.get_template("index.html")
template_users = env.get_template("users.html")
template_currencies = env.get_template("currencies.html")
template_author = env.get_template("author.html")
template_user = env.get_template("user.html")
```
### Интеграция функции get_currencies
Для получения актуальных курсов валют используется функция get_currencies из прошлой лабораторной работы.

Загрузка всех валют из API выполняется функцией:
```python
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
```
## Скриншоты страниц
### Главная страница
![main](static/images/main.png)

### Пользователи
![users](static/images/users.png)

### Курсы валют
![currencies](static/images/currencies.png)

## Тестирование
## Выводы

### Ефимов Сергей Робертович, 2 курс, ИВТ-2



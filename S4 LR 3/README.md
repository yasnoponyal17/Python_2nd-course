# Лабораторная работа 3. Разработка REST API для отслеживания курсов валют (FastAPI + SQLAlchemy)
## Цель работы
Разработать асинхронное веб-приложение (REST API) с использованием фреймворка FastAPI и библиотеки SQLAlchemy (в качестве ORM) для взаимодействия с базой данных SQLite. Приложение должно предоставлять функционал регистрации пользователей и подписки на отслеживание актуальных курсов валют, получаемых от Центрального банка РФ.
## Структура проекта
```
currency_tracker/
├── models/
│   ├── __init__.py
│   ├── user.py
│   ├── currency.py
│   └── subscription.py
├── schemas/
│   ├── __init__.py
│   ├── user.py
│   ├── currency.py
│   └── subscription.py
├── routers/
│   ├── __init__.py
│   ├── users.py
│   ├── currencies.py
│   └── subscriptions.py
├── services/
│   └── __init__.py
├── database.py
├── main.py
└── requirements.txt
```
## Как запустить
### Установка
```bash
pip install -r requirements.txt
```
### Запуск
```bash
uvicorn main:app --reload
```
### Документация
Открыть в браузере http://127.0.0.1:8000/docs
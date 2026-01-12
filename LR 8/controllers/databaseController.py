import sqlite3
from models.user import User
from models.currency import Currency

class CurrencyRatesCRUD:
    def __init__(self):
        self.conn = sqlite3.connect(':memory:', check_same_thread=False)
        self.conn.row_factory = sqlite3.Row
        self._create_tables()

    def _create_tables(self):
        cursor = self.conn.cursor()
        cursor.executescript('''
            CREATE TABLE user (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL
            );

            CREATE TABLE currency (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                num_code TEXT NOT NULL,
                char_code TEXT NOT NULL,
                name TEXT NOT NULL,
                value FLOAT,
                nominal INTEGER
            );

            CREATE TABLE user_currency (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                currency_id INTEGER NOT NULL,
                FOREIGN KEY(user_id) REFERENCES user(id),
                FOREIGN KEY(currency_id) REFERENCES currency(id)
            );
        ''')
        cursor.executemany("INSERT INTO user (name) VALUES (?)", 
                           [("Ким Чен Ын",), ("OG Buda",), ("Субо братик",), ("Папич",)])
        self.conn.commit()

    def _create_currency(self, currency_data):
        sql = """INSERT INTO currency(num_code, char_code, name, value, nominal) 
                 VALUES(:num_code, :char_code, :name, :value, :nominal)"""
        self.conn.cursor().execute(sql, currency_data)
        self.conn.commit()

    def _read(self):
        return self.conn.execute("SELECT * FROM currency").fetchall()

    def _update(self, char_code, new_value):
        sql = "UPDATE currency SET value = ? WHERE char_code = ?"
        self.conn.execute(sql, (new_value, char_code))
        self.conn.commit()

    def _delete(self, currency_id):
        sql = "DELETE FROM currency WHERE id = ?"
        self.conn.execute(sql, (currency_id,))
        self.conn.commit()

    def get_user_subscriptions(self, user_id):
        sql = '''SELECT c.* FROM currency c 
                 JOIN user_currency uc ON c.id = uc.currency_id 
                 WHERE uc.user_id = ?'''
        return self.conn.execute(sql, (user_id,)).fetchall()
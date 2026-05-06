import sqlite3

from utils.currencies_api import get_currencies

class DatabaseController:
    def __init__(self):
        self.conn = sqlite3.connect(':memory:')
        self.conn.row_factory = sqlite3.Row
        self.cursor = self.conn.cursor()
        self.cursor.execute("PRAGMA foreign_keys = ON")

        self._create_tables()
        self._seed()

    def _create_tables(self):
        self.cursor.execute("""CREATE TABLE user 
                            (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                            name TEXT NOT NULL
                            )""")
        self.cursor.execute("""CREATE TABLE currency 
                            (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                            num_code INTEGER,
                            char_code TEXT NOT NULL,
                            name TEXT NOT NULL,
                            value FLOAT,
                            nominal INTEGER
                            )
                            """)
        self.cursor.execute("""CREATE TABLE user_currency 
                            (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                            user_id INTEGER NOT NULL,
                            currency_id INTEGER NOT NULL,
                            FOREIGN KEY(user_id) REFERENCES user(id), 
                            FOREIGN KEY(currency_id) REFERENCES currency(id)
                            )""")

    def _seed(self):
        data = get_currencies()
    
        self.cursor.execute("INSERT INTO user (id, name) VALUES (?, ?)", (1, 'Кто-то'))
        self.cursor.execute("INSERT INTO user (id, name) VALUES (?, ?)", (2, 'Ещё кто-то'))

        for curr in data.values():
            self.cursor.execute(
                "INSERT INTO currency (num_code, char_code, name, value, nominal) VALUES (?, ?, ?, ?, ?)",
                (curr['num_code'], curr['char_code'], curr['name'], curr['value'], curr['nominal'])
            )

        self.cursor.execute("SELECT id FROM currency WHERE char_code = ?", ('USD',))
        usd_id = self.cursor.fetchone()['id']
        self.cursor.execute("INSERT INTO user_currency (id, user_id, currency_id) VALUES (?, ?, ?)", (1, 1, usd_id))

        self.cursor.execute("SELECT id FROM currency WHERE char_code = ?", ('EUR',))
        eur_id = self.cursor.fetchone()['id']
        self.cursor.execute("INSERT INTO user_currency (id, user_id, currency_id) VALUES (?, ?, ?)", (2, 1, eur_id))

        self.cursor.execute("SELECT id FROM currency WHERE char_code = ?", ('GBP',))
        gbp_id = self.cursor.fetchone()['id']
        self.cursor.execute("INSERT INTO user_currency (id, user_id, currency_id) VALUES (?, ?, ?)", (3, 2, gbp_id))
        
        self.cursor.execute("SELECT id FROM currency WHERE char_code = ?", ('JPY',))
        jpy_id = self.cursor.fetchone()['id']
        self.cursor.execute("INSERT INTO user_currency (id, user_id, currency_id) VALUES (?, ?, ?)", (4, 2, jpy_id))

        self.conn.commit()

    def _read_currencies(self):
        self.cursor.execute("SELECT * FROM currency")
        return self.cursor.fetchall()
    
    def _delete_currencies(self, currency_id):
        self.cursor.execute("DELETE FROM currency WHERE id = ?", (currency_id, ))
        self.conn.commit()

    def _update_currencies(self, char_code, value):
        self.cursor.execute("UPDATE currency SET value = ? WHERE char_code = ?", (value, char_code))
        self.conn.commit()
    
    def _create_currencies(self, num_code, char_code, name, value, nominal):
        self.cursor.execute("INSERT INTO currency (num_code, char_code, name, value, nominal) VALUES (?, ?, ?, ?, ?)", (num_code, char_code, name, value, nominal))
        self.conn.commit()

    def _read_users(self):
        self.cursor.execute("SELECT * FROM user")
        return self.cursor.fetchall()

    def _read_user_currencies(self, user_id):
        self.cursor.execute("SELECT currency.* FROM currency JOIN user_currency ON currency.id = user_currency.currency_id WHERE user_currency.user_id = ?", (user_id, ))
        return self.cursor.fetchall()
    
    def _get_user(self, user_id):
        self.cursor.execute("SELECT * FROM user WHERE id = ?", (user_id, ))
        return self.cursor.fetchone()
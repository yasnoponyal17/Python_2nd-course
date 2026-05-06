from controllers.databaseController import DatabaseController

class CurrenciesController:
    def __init__(self, db: DatabaseController):
        self.db = db

    def list_currencies(self):
        return self.db._read_currencies()
    
    def delete_currency(self, currency_id):
        self.db._delete_currencies(currency_id)

    def update_currency(self, char_code, value):
        self.db._update_currencies(char_code, value)
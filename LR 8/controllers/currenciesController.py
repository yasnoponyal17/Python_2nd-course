from models.currency import Currency

class CurrenciesController:
    def __init__(self, db_controller):
        self.db = db_controller

    def list_currencies(self):
        return self.db._read()

    def update_currency(self, char_code, value):
        self.db._update(char_code, value)

    def delete_currency(self, currency_id):
        self.db._delete(currency_id)
        
    def add_from_api(self, api_data):
        for item in api_data:
            self.db._create_currency(item)
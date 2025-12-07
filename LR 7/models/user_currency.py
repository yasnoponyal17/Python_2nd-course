class UserCurrency:
    def __init__(self, id, user_id, currency_id):
        self.id = id
        self.user_id = user_id
        self.currency_id = currency_id
        
    def id(self):
        return self._id
    
    def id(self, value):
        if (value <= 0):
            raise ValueError("Идентификатор не должен быть отрицательным.")
        self._id = value
        
    def user_id(self):
        return self._user_id
    
    def user_id(self, value):
        if (value <= 0):
            raise ValueError("Идентификатор пользователя не должен быть отрицательным.")
        self._user_id = value
        
    def currency_id(self):
        return self._currency_id
    
    def currency_id(self, value):
        if (value <= 0):
            raise ValueError("Идентификатор валюты не должен быть отрицательным.")
        self._currency_id = value
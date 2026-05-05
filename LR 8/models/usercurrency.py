class UserCurrency:
    def __init__(self, id, user_id, currency_id):
        self.__id = id
        self.__user_id = user_id
        self.__currency_id = currency_id
        
    @property
    def id(self):
        return self.__id
    
    @id.setter
    def id(self, id):
        if isinstance(id, int):
            self.__id = id
        else:
            print("Идентификатор должен быть целым числом.")
            
    @property
    def user_id(self):
        return self.__user_id
    
    @user_id.setter
    def user_id(self, user_id):
        if isinstance(user_id, int):
            self.__user_id = user_id
        else:
            print("Идентификатор пользователя должен быть целым числом.")
            
    @property
    def currency_id(self):
        return self.__currency_id
    
    @currency_id.setter
    def currency_id(self, currency_id):
        if isinstance(currency_id, str):
            self.__currency_id = currency_id
        else:
            print("Идентификатор валюты должен быть строкой.")
        
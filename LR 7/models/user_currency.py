class UserCurrency:
    def __init__(self, id: int, user_id: int, currency_id: str):
        self.id = id
        self.user_id = user_id
        self.currency_id = currency_id
        
    @property
    def id(self) -> int:
        return self._id
    
    @id.setter
    def id(self, id: int):
        if not isinstance(id, int):
            raise TypeError('ID должен быть целым числом')
        if id < 0:
            raise ValueError('ID должен быть положительным числом')
        self._id = id

    @property
    def user_id(self) -> int:
        return self._user_id
    
    @user_id.setter
    def user_id(self, user_id: int):
        if not isinstance(user_id, int):
            raise TypeError('User ID должен быть целым числом')
        if user_id < 0:
            raise ValueError('User ID должен быть положительным числом')
        self._user_id = user_id

    @property
    def currency_id(self) -> str:
        return self._currency_id

    @currency_id.setter
    def currency_id(self, currency_id: str):
        if not isinstance(currency_id, str):
            raise TypeError('Сurrency ID должен быть строкой')
        if currency_id.strip() == '':
            raise ValueError('Currency ID не может быть пустым значением')
        self._currency_id = currency_id
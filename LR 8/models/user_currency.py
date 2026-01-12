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
        self._id = id

    @property
    def user_id(self) -> int:
        return self._user_id
    
    @user_id.setter
    def user_id(self, user_id: int):
        self._user_id = user_id

    @property
    def currency_id(self) -> str:
        return self._currency_id

    @currency_id.setter
    def currency_id(self, currency_id: str):
        self._currency_id = currency_id
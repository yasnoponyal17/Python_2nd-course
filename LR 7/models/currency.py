class Currency:
    def __init__(self, id: str, num_code: int, char_code: str, name: str, value: float, nominal: int):
        self.id = id
        self.num_code = num_code
        self.char_code = char_code
        self.name = name
        self.value = value
        self.nominal = nominal
        
    @property
    def id(self) -> str:
        return self._id
    
    @id.setter
    def id(self, id: str):
        if not isinstance(id, str):
            raise TypeError('ID должно быть строкой')
        if id.strip() == '':
            raise ValueError('ID не может быть пустым значением')
        self._id = id

    @property
    def num_code(self) -> int:
        return self._num_code
    
    @num_code.setter
    def num_code(self, num_code: int):
        if not isinstance(num_code, int):
            raise TypeError('Цифровой код должен быть целым числом')
        if num_code < 0:
            raise ValueError('Цифровой код не может быть отрицательным')
        self._num_code = num_code

    @property
    def char_code(self) -> str:
        return self._char_code
    
    @char_code.setter
    def char_code(self, char_code: str):
        if not isinstance(char_code, str):
            raise TypeError('Символьный код должен быть строкой')
        if char_code.strip() == '':
            raise ValueError('Символьный код не может быть пустым значением')
        self._char_code = char_code

    @property
    def name(self) -> str:
        return self._name
    
    @name.setter
    def name(self, name: str):
        if not isinstance(name, str):
            raise TypeError('Название должно быть строкой')
        if name.strip() == '':
            raise ValueError('Название не может быть пустым значением')
        self._name = name

    @property
    def value(self) -> float:
        return self._value
    
    @value.setter
    def value(self, value: float):
        if not isinstance(value, float):
            raise TypeError('Курс должен быть числом')
        if value <= 0:
            raise ValueError('Курс должен быть положительным числом')
        self._value = value

    @property
    def nominal(self) -> int:
        return self._nominal

    @nominal.setter
    def nominal(self, nominal: int):
        if not isinstance(nominal, int):
            raise TypeError('Номинал должен быть целым числом')
        if nominal <= 0:
            raise ValueError('Номинал должен быть положительным числом')
        self._nominal = nominal
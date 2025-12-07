class Currency:
    def __init__(self, id, num_code, char_code, name, value, nominal):
        self.id = id
        self.num_code = num_code
        self.char_code = char_code
        self.name = name
        self.value = value
        self.nominal = nominal
        
    def id(self):
        return self._id
    
    def id(self, value):
        if (len(value) == 0):
            raise ValueError("Идентификатор не должен быть пустым.")
        self._id = value
        
    def num_code(self):
        return self._num_code
    
    def num_code(self, value):
        if (value <= 0):
            raise ValueError("Цифровой код не должен быть отрицательным.")
        self._num_code = value
        
    def char_code(self):
        return self._char_code
    
    def char_code(self, value):
        if (len(value) == 0):
            raise ValueError("Символьный код не должен быть пустым.")
        self._char_code = value
        
    def name(self):
        return self._name
    
    def name(self, value):
        if (len(value) == 0):
            raise ValueError("Название валюты не должно быть пустым.")
        self._name = value
        
    def value(self):
        return self._value
    
    def value(self, val):
        if (val <= 0):
            raise ValueError("Курс валюты не должен быть отрицательным.")
        self._value = val
        
    def nominal(self):
        return self._nominal
    
    def nominal(self, value):
        if (value <= 0):
            raise ValueError("Номинал не должен быть отрицательным.")
        self._nominal = value
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
        self._id = id

    @property
    def num_code(self) -> int:
        return self._num_code
    
    @num_code.setter
    def num_code(self, num_code: int):
        self._num_code = num_code

    @property
    def char_code(self) -> str:
        return self._char_code
    
    @char_code.setter
    def char_code(self, char_code: str):
        self._char_code = char_code

    @property
    def name(self) -> str:
        return self._name
    
    @name.setter
    def name(self, name: str):
        self._name = name

    @property
    def value(self) -> float:
        return self._value
    
    @value.setter
    def value(self, value: float):
        self._value = value

    @property
    def nominal(self) -> int:
        return self._nominal

    @nominal.setter
    def nominal(self, nominal: int):
        self._nominal = nominal
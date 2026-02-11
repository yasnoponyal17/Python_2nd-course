class User:
    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name
        
    @property
    def id(self) -> int:
        return self._id
    
    @id.setter
    def id(self, id: int):
        if not isinstance(id, int):
            raise TypeError('ID должно быть целым числом')
        if id < 0:
            raise ValueError('ID не может быть отрицательным')
        self._id = id

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name: str):
        if not isinstance(name, str):
            raise TypeError('Имя должно быть строкой')
        if name.strip() == '':
            raise ValueError('Имя не может быть пустым значением')
        self._name = name
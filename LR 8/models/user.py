class User:
    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name
        
    @property
    def id(self) -> int:
        return self._id
    
    @id.setter
    def id(self, id: int):
        self._id = id

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name: str):
        self._name = name
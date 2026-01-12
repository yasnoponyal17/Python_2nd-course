class Author:
    def __init__(self, name: str, group: str):
        self.name = name
        self.group = group
        
    @property
    def name(self) -> str:
        return self._name

    @property
    def group(self) -> str:
        return self._group
    
    @name.setter
    def name(self, name: str):
        self._name = name

    @group.setter
    def group(self, group: str):
        self._group = group
        
    
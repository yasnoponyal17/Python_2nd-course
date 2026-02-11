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
        if not isinstance(name, str):
            raise TypeError('Имя должно быть строкой')
        if name.strip() == '':
            raise ValueError('Имя не может быть пустым значением')
        self._name = name

    @group.setter
    def group(self, group: str):
        if not isinstance(group, str):
            raise TypeError('Имя должно быть строкой')
        if group.strip() == '':
            raise ValueError('Имя не может быть пустым значением')
        self._group = group
        
    
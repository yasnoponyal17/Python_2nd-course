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
<<<<<<< Updated upstream
            raise TypeError('Имя должно быть строкой')
        if name.strip() == '':
            raise ValueError('Имя не может быть пустым значением')
=======
            raise TypeError("Имя должно быть строкой")
        if name.strip() == '':
            raise ValueError("Имя не может быть пустым")
>>>>>>> Stashed changes
        self._name = name

    @group.setter
    def group(self, group: str):
        if not isinstance(group, str):
<<<<<<< Updated upstream
            raise TypeError('Имя должно быть строкой')
        if group.strip() == '':
            raise ValueError('Имя не может быть пустым значением')
=======
            raise TypeError('Группа должна быть строкой')
        if group.strip() == '':
            raise ValueError('Группа не может быть пустой')
>>>>>>> Stashed changes
        self._group = group
        
    
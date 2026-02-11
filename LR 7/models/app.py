from models.author import Author

class App:
    def __init__(self, name: str, version: str, author: Author):
        self.name = name
        self.version = version
        self.author = author
        
    @property
    def name(self) -> str:
        return self._name
    
    @property
    def version(self) -> str:
        return self._version
    
    @property
    def author(self) -> Author:
        return self._author
    
    @name.setter
    def name(self, name: str):
        if not isinstance(name, str):
            raise TypeError('Название должно быть строкой')
        if name.strip() == '':
            raise ValueError('Название не может быть пустым значением')
        self._name = name
        
    @version.setter
    def version(self, version: str):
        if not isinstance(version, str):
            raise TypeError('Версия должна быть строкой')
        if version.strip() == '':
            raise ValueError('Версия не может быть пустым значением')
        self._version = version

    @author.setter
    def author(self, author: Author):
        if not isinstance(author, Author):
            raise TypeError("Автор должен быть объектом")
        self._author = author
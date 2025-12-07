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
        self._name = name
        
    @version.setter
    def version(self, version: str):
        self._version = version

    @author.setter
    def author(self, author: Author):
        self._author = author
from models.author import Author

class App:
    def __init__(self, name, version, author: Author):
        self.__name = name
        self.__version = version
        self.__author = author
        
    @property
    def name(self):
        return self.__name
            
    @name.setter
    def name(self, name):
        if isinstance(name, str):
            self.__name = name
        else:
            print("Название приложения должно быть строкой.")
            
    @property
    def version(self):
        return self.__version
    
    @version.setter
    def version(self, version):
        if isinstance(version, str):
            self.__version = version
        else:
            print("Версия приложения должна быть строкой.")
            
    @property
    def author(self):
        return self.__author
    
    @author.setter
    def author(self, author):
        if isinstance(author, Author):
            self.__author = author
        else:
            print("Автор должен быть объектом.")
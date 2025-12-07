class App:
    def __init__(self, name, version, author: Author):
        self.name = name
        self.version = version
        self.author = author
        
    def name(self):
        return self._name
    
    def name(self, value):
        if (len(value) == 0):
            raise ValueError("Название приложения не должно быть пустым.")
        self._name = value
    
    def version(self):
        return self._version
    
    def version(self, value):
        if (len(value) == 0):
            raise ValueError("Версия приложения не должна быть пустой.")
        self._version = value
    
    def author(self):
        return self._author
    
    def author(self, value):
        if not isinstance(value, Author):
            raise TypeError("App.author должен быть объектом Author.")
        self._author = value
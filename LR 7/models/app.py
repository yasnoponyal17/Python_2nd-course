class App:
    def __init__(self, name, version, author):
        self.name = name
        self.version = version
        self.author = author
        
    def name(self):
        return self._name
    
    def name(self, value):
        if (len(value) < 3):
            raise ValueError("Имя должно быть длиннее 3 символов.")
        self._name = value
    
    def version(self):
        return self._version
    
    def version(self, value):
        if (len(value) < 3):
            raise ValueError("Имя версии должно быть длиннее 3 символов.")
        self._version = value
    
    def author(self):
        return self._author
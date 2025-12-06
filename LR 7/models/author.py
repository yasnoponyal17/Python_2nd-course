class Author:
    def __init__(self, name, group):
        self.name = name
        self.group = group
        
    def name(self):
        return self._name
    
    def name(self, value):
        if (len(value) <= 3):
            raise ValueError("Имя должно быть длиннее 3 символов.")
        self._name = value
        
    def group(self):
        return self._group
    
    def group(self, value):
        if (len(value) < 1):
            raise ValueError("Название группы не должно быть пустым.")
        self._group = value
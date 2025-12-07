class Author:
    def __init__(self, name, group):
        self.name = name
        self.group = group
        
    def name(self):
        return self._name
    
    def name(self, value):
        if (len(value) == 0):
            raise ValueError("Имя автора не должно быть пустым.")
        self._name = value
        
    def group(self):
        return self._group
    
    def group(self, value):
        if (len(value) == 0):
            raise ValueError("Учебная группа не должна быть пустой.")
        self._group = value
class User:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        
        def id(self):
            self._id
            
        def id(self, value):
            if (len(value) < 3):
                raise ValueError("Идентификатор не должен быть меньше 3 символов.")
            self._id = value
            
        def name(self):
            self._name
            
        def name(self, value):
            if (len(value) < 3):
                raise ValueError("Имя не должно быть меньше 3 символов.")
            self._name = value
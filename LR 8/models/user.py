class User:
    def __init__(self, id, name):
        self.__id = id
        self.__name = name
        
    @property
    def id(self):
        return self.__id
    
    @id.setter
    def id(self, id):
        if isinstance(id, int):
            self.__id = id
        else:
            print("Идентификатор пользователя должен быть целым числом.")
            
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str):
            self.__name = name
        else:
            print("Имя пользователя должно быть строкой.")
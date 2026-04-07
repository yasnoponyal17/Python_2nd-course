class Author:
    def __init__(self, name, group):
        self.__name = name
        self.__group = group
        
    @property        
    def name(self):
        return self.__name
    
    @name.setter    
    def name(self, name):
        if isinstance(name, str):
            self.__name = name
        else:
            print("Имя автора должно быть строкой")
            
    @property
    def group(self):
        return self.__group
    
    @group.setter        
    def group(self, group):
        if isinstance(group, str):
            self.__group = group
        else:
            print("Учебная группа должна быть строкой.")
    
    
    
    
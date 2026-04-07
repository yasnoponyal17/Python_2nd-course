class Currency:
    def __init__(self, id, num_code, char_code, name, value, nominal):
        self.__id = id
        self.__num_code = num_code
        self.__char_code = char_code
        self.__name = name
        self.__value = value
        self.__nominal = nominal
        
    @property
    def id(self):
        return self.__id
    
    @id.setter
    def id(self, id):
        if isinstance(id, str):
            self.__id = id
        else:
            print("Идентификатор валюты должен быть строкой.")
            
    @property
    def num_code(self):
        return self.__num_code
    
    @num_code.setter
    def num_code(self, num_code):
        if isinstance(num_code, int):
            self.__num_code = num_code
        else:
            print("Цифровой код должен быть целым числом.")
            
    @property
    def char_code(self):
        return self.__char_code
    
    @char_code.setter
    def char_code(self, char_code):
        if isinstance(char_code, str):
            self.__char_code = char_code
        else:
            print("Символьный код должен быть строкой.")
            
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str):
            self.__name = name
        else:
            print("Название валюты должно быть строкой.")
            
    @property
    def value(self):
        return self.__value
    
    @value.setter
    def value(self, value):
        if isinstance(value, float):
            self.__value = value
        else:
            print("Курс валюты должен быть числом с плавающей точкой.")
            
    @property
    def nominal(self):
        return self.__nominal
    
    @nominal.setter
    def nominal(self, nominal):
        if isinstance(nominal, int):
            self.__nominal = nominal
        else:
            print("Номинал должен быть целым числом.")
    
    
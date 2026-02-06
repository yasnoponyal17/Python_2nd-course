class FibonacciIterator:
    def __init__(self, instance):
        """
        Инициализирует итератор.

        Аргументы:
            instance - Итерируемый объект с числами.
        """
        self.instance = instance
        self.index = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        """
        Возвращает следующее число Фибоначчи из последовательности.

        Ищет в self.instance число, начиная с текущего self.index.
        Если число не является числом Фибоначчи, переходит к следующему.

        Возвращает:
            Следующее найденное число Фибоначчи.

        Исключения:
            StopIteration - Когда элементы в self.instance закончились.
        """
        while True:
            try:
                number = self.instance[self.index]
            except IndexError:
                raise StopIteration
            
            a = 0
            b = 1
            
            while a < number:
                c = a + b
                a = b
                b = c
                
            self.index += 1
                
            if a == number:
                return number
                
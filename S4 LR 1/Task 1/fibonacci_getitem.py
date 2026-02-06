class FibonacciGetItem:
    def __init__(self, instance):
        """
        Инициализирует объект и фильтрует входную последовательность.

        Аргументы:
            instance - Итерируемый объект с целыми числами.
        """
        self.fibonacci_list = []
        
        for number in instance:
            if self._is_fibonacci(number):
                self.fibonacci_list.append(number) 
    
    def _is_fibonacci(self, n):
        """
        Проверяет, является ли целое число числом Фибоначчи.

        Аргументы:
            n - целое число для проверки.

        Возвращает:
            True - если число принадлежит ряду Фибоначчи
            False - если не принадлежит
        """
        a = 0
        b = 1
        
        while a < n:
            c = a + b
            a = b
            b = c
            
        if a == n:
            return True
    
    def __getitem__(self, index):
        """
        Возвращает элемент из отфильтрованного списка по индексу.

        Аргументы:
            index - Порядковый номер элемента.

        Возвращает:
            Число Фибоначчи.
        """
        return self.fibonacci_list[index]

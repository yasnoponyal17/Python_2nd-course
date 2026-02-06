# Лабораторная работа 1. Итераторы, генераторы, сопрограммы.
## Постановка задачи
Задание 1. Создание программы, возвращающей список чисел Фибоначчи с помощью итератора (2 способа).

Задание 2. Создание сопрограммы на основе кода, позволяющей по данному n сгенерировать список элементов из ряда Фибоначчи.

## Код задания 1
### Способ 1
```python
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
```

### Способ 2
```python
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
```

## Код задания 2
```python
import functools

def fibonacci_generator():
    """
    Сопрограмма для генерации списков чисел Фибоначчи.

    В бесконечном цикле ожидает передачи целого числа n через метод send().
    После получения n генерирует список из первых n элементов ряда Фибоначчи
    и возвращает его через yield.
    """

    while True:
        number_of_fib_elem = yield
        
        fibonacci_list = []
        a = 0
        b = 1
        
        for _ in range(number_of_fib_elem):
            fibonacci_list.append(a)
            c = a + b
            a = b
            b = c
            
        yield fibonacci_list

def fibonacci_coroutine(g):
    @functools.wraps(g)
    def inner(*args, **kwargs):
        gen = g(*args, **kwargs)
        gen.send(None)
        return gen
    return inner
```

## Тестирование
### Задание 1
```python
import unittest

from fibonacci_iterator import FibonacciIterator
from fibonacci_getitem import FibonacciGetItem

class TestIterator(unittest.TestCase):
    def test_1(self):
        self.assertEqual(list(FibonacciIterator(range(10))), [0, 1, 2, 3, 5, 8])
        self.assertEqual(list(FibonacciGetItem(range(10))), [0, 1, 2, 3, 5, 8])
        
    def test_2(self):
        self.assertEqual(list(FibonacciIterator(range(1))), [0])
        self.assertEqual(list(FibonacciGetItem(range(1))), [0])
        
    def test_3(self):
        self.assertEqual(list(FibonacciIterator(range(67))), [0, 1, 2, 3, 5, 8, 13, 21, 34, 55])
        self.assertEqual(list(FibonacciGetItem(range(67))), [0, 1, 2, 3, 5, 8, 13, 21, 34, 55])
        
    def test_4(self):
        self.assertEqual(list(FibonacciIterator(range(0))), [])
        self.assertEqual(list(FibonacciGetItem(range(0))), [])
        
unittest.main(verbosity=2)    
```
### Задание 2
```python
import unittest

from fibonacci_coroutine import fibonacci_generator, fibonacci_coroutine

class TestCoroutine(unittest.TestCase):
    def setUp(self):
        self.gen = fibonacci_coroutine(fibonacci_generator)()
        
    def test_1(self):
        self.assertEqual(self.gen.send(5), [0, 1, 1, 2, 3])
        
    def test_2(self):
        self.assertEqual(self.gen.send(1), [0])
        
    def test_3(self):
        self.assertEqual(self.gen.send(0), [])
        
unittest.main(verbosity=2)
```

### Ефимов Сергей Робертович, 2 курс, ИВТ-2
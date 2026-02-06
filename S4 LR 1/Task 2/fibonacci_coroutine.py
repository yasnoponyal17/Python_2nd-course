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
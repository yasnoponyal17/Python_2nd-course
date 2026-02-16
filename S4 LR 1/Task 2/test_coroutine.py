import unittest

from fibonacci_coroutine import fibonacci_generator, fibonacci_coroutine

class TestCoroutine(unittest.TestCase):
        
    def test_1(self):
        gen = fibonacci_coroutine(fibonacci_generator)()
        self.assertEqual(gen.send(5), [0, 1, 1, 2, 3])
        
    def test_2(self):
        gen = fibonacci_coroutine(fibonacci_generator)()
        self.assertEqual(gen.send(1), [0])
        
    def test_3(self):
        gen = fibonacci_coroutine(fibonacci_generator)()
        self.assertEqual(gen.send(0), [])
        
unittest.main(verbosity=2)
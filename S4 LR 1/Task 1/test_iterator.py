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
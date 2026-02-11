import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from models.currency import Currency

class TestCurrency(unittest.TestCase):
    def test_getter(self):
        currency = Currency('R01235', 840, 'USD', 'Доллар США', 75.5, 1)
        self.assertEqual(currency.id, 'R01235')
        self.assertEqual(currency.num_code, 840)
        self.assertEqual(currency.char_code, "USD")
        self.assertEqual(currency.name, "Доллар США")
        self.assertEqual(currency.value, 75.5)
        self.assertEqual(currency.nominal, 1)
        
    def test_setter(self):
        currency = Currency('R01235', 840, 'USD', 'Доллар США', 75.5, 1)
        currency.id = "R00000"
        currency.num_code = 322
        currency.char_code = 'LOL'
        currency.name = 'Тут должно быть что-то смешное'
        currency.value = 67.52
        currency.nominal = 10
        self.assertEqual(currency.id, 'R00000')
        self.assertEqual(currency.num_code, 322)
        self.assertEqual(currency.char_code, "LOL")
        self.assertEqual(currency.name, "Тут должно быть что-то смешное")
        self.assertEqual(currency.value, 67.52)
        self.assertEqual(currency.nominal, 10)
        
    def test_type_error(self):
        with self.assertRaises(TypeError):
            Currency(5000, 840, 'USD', 'Доллар США', 75.5, 1)
            
        with self.assertRaises(TypeError):
            Currency('R01235', 840.10101010101, 'USD', 'Доллар США', 75.5, 1)
            
        with self.assertRaises(TypeError):
            Currency('R01235', 840, 0, 'Доллар США', 75.5, 1)
        
        with self.assertRaises(TypeError):
            Currency('R01235', 840, 'USD', 0, 75.5, 1)
            
        with self.assertRaises(TypeError):
            Currency('R01235', 840, 'USD', 'Доллар США', '75.5', 1)
            
        with self.assertRaises(TypeError):
            Currency('R01235', 840, 'USD', 'Доллар США', 75.5, 1.2)
            
    def test_value_error(self):
        with self.assertRaises(ValueError):
            Currency('', 840, 'USD', 'Доллар США', 75.5, 1)
            
        with self.assertRaises(ValueError):
            Currency('R01235', -840, 'USD', 'Доллар США', 75.5, 1)
            
        with self.assertRaises(ValueError):
            Currency('R01235', 840, '', 'Доллар США', 75.5, 1)
            
        with self.assertRaises(ValueError):
            Currency('R01235', 840, 'USD', '', 75.5, 1)
            
        with self.assertRaises(ValueError):
            Currency('R01235', 840, 'USD', 'Доллар США', -75.5, 1)
            
        with self.assertRaises(ValueError):
            Currency('R01235', 840, 'USD', 'Доллар США', 75.5, 0)
        
unittest.main(verbosity=2)
        
        
        
        
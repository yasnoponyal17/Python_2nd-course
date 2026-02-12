import unittest
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from models.user_currency import UserCurrency

class TestUserCurrency(unittest.TestCase):
    def test_getter(self):
        usercurrency = UserCurrency(14, 88, "R01235")
        self.assertEqual(usercurrency.id, 14)
        self.assertEqual(usercurrency.user_id, 88)
        self.assertEqual(usercurrency.currency_id, "R01235")
    
    def test_setter(self):
        usercurrency = UserCurrency(14, 88, "R01235")
        usercurrency.id = 192
        usercurrency.user_id = 89
        usercurrency.currency_id = "R01234"
        self.assertEqual(usercurrency.id, 192)
        self.assertEqual(usercurrency.user_id, 89)
        self.assertEqual(usercurrency.currency_id, "R01234")
        
    def test_type_error(self):
        with self.assertRaises(TypeError):
            UserCurrency('14', 88, "R01235")
        
        with self.assertRaises(TypeError):
            UserCurrency(14, '88', 'R01235')
            
        with self.assertRaises(TypeError):
            UserCurrency(14, 88, True)
            
    def test_value_error(self):
        with self.assertRaises(ValueError):
            UserCurrency(-111, 11, "R01111")
        
        with self.assertRaises(ValueError):
            UserCurrency(1, -2, "R01234")
            
        with self.assertRaises(ValueError):
            UserCurrency(1, 2, "")
        
unittest.main(verbosity=2)
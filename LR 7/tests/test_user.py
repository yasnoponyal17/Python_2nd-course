import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from models.user import User

class TestUser(unittest.TestCase):
    def test_getter(self):
        user = User(1, "Меллстрой")
        self.assertEqual(user.id, 1)
        self.assertEqual(user.name, 'Меллстрой')
        
    def test_setter(self):
        user = User(1, 'Меллстрой')
        user.id = 228
        user.name = 'the fog'
        self.assertEqual(user.id, 228)
        self.assertEqual(user.name, 'the fog')
        
    def test_type_error(self):
        with self.assertRaises(TypeError):
            User('1', 'Меллстрой')
        
        with self.assertRaises(TypeError):
            User(1.0000000000000001, 'Дима Коляденко')
            
        with self.assertRaises(TypeError):
            User(666, 777)
            
    def test_value_error(self):
        with self.assertRaises(ValueError):
            User(-1000, 'Илюха Монеси')
            
        with self.assertRaises(ValueError):
            User(67, '')
            
        with self.assertRaises(ValueError):
            User(69, '        ')
      
        
unittest.main(verbosity=2)
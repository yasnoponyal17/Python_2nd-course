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
        
unittest.main(verbosity=2)
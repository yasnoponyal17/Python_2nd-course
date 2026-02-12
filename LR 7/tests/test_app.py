import unittest
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from models.app import App
from models.author import Author

class TestApp(unittest.TestCase):
    def setUp(self):
        self.author = Author('Роберт Плаудис', "РНБ КЛУБ")
    
    def test_getter(self):
        app = App("TheBestAppNoCap", "1.5.2", self.author)
        self.assertEqual(app.name, "TheBestAppNoCap")
        self.assertEqual(app.version, "1.5.2")
        self.assertEqual(app.author, self.author)
        
    def test_setter(self):
        app = App("TheBestAppNoCap", "1.5.2", self.author)
        new_author = Author('Константин Смоляр', 'Без лейбла...')
        app.name = "TheWorstAppInTheWorld"
        app.version = "1.21.9"
        app.author = new_author
        self.assertEqual(app.name, "TheWorstAppInTheWorld")
        self.assertEqual(app.version, "1.21.9")
        self.assertEqual(app.author, new_author)
        
    def test_type_error(self):
        with self.assertRaises(TypeError):
            App(7, "1.12.2", self.author)
            
        with self.assertRaises(TypeError):
            App("AppAppApp", 1234567890, self.author)
        
        with self.assertRaises(TypeError):
            App("Hello", "hru?", "Goodbye")
            
    def test_value_error(self):
        with self.assertRaises(ValueError):
            App('', "XJHGSJKDHGBNJKSDGHNSJKDGBNSDKJG", self.author)
            
        with self.assertRaises(ValueError):
            App("something", '', self.author)
        
unittest.main(verbosity=2)
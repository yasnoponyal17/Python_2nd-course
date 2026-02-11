import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from models.author import Author

class TestAuthor(unittest.TestCase):
    def test_getter(self):
        author = Author('Данил Колбасенко', 'Стандофф 2')
        self.assertEqual(author.name, 'Данил Колбасенко')
        self.assertEqual(author.group, 'Стандофф 2')
        
    def test_setter(self):
        author = Author('Артур', 'Группа 1')
        author.name = 'Привет, Артур'
        author.group = 'Hi!'
        self.assertEqual(author.name, 'Привет, Артур')
        self.assertEqual(author.group, 'Hi!')
        
    def test_type_error(self):
        with self.assertRaises(TypeError):
            Author(1337, 'Группа топовых чисел')
            
        with self.assertRaises(TypeError):
            Author('Код10', 80)
            
    def test_value_error(self):
        with self.assertRaises(ValueError):
            Author("", "крутецкая круть")
        
        with self.assertRaises(ValueError):
            Author("    ", "Пробелпробелпробелпробел")
            
        with self.assertRaises(ValueError):
            Author("Кьо этость?", "")
        
        with self.assertRaises(ValueError):
            Author("Зайчик Джуди Хопс", "      ")
            
unittest.main(verbosity=2)
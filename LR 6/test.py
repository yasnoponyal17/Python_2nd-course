import unittest
import io
from iteration1 import get_currencies

MAX_R_VALUE = 1000

class TestGetCurrencies(unittest.TestCase):

    def test_currency_usd(self):
        currency_list = ['USD']
        currency_data = get_currencies(currency_list)

        self.assertIn(currency_list[0], currency_data)
        self.assertIsInstance(currency_data['USD'], float)
        self.assertGreaterEqual(currency_data['USD'], 0)
        self.assertLessEqual(currency_data['USD'], MAX_R_VALUE)

    def test_nonexist_code(self):
        result = get_currencies(['XYZ'])
        self.assertNotIn('XYZ', result)
        self.assertEqual(result, {})

    def test_get_currency_error(self):
        error_phrase_regex = "Ошибка при выполнении запроса"
        currency_list = ['USD']
        captured_output = io.StringIO()
        
        result = get_currencies(currency_list, url="https://", handle=captured_output)
        
        output = captured_output.getvalue()
        self.assertIn(error_phrase_regex, output)
        self.assertIsNone(result)

    def test_error_starts_with_phrase(self):
        error_phrase = "Ошибка при выполнении запроса"
        currency_list = ['USD']
        captured_output = io.StringIO()
        
        result = get_currencies(currency_list, url="https://", handle=captured_output)
        
        output = captured_output.getvalue()
        self.assertTrue(output.startswith(error_phrase))

    def test_nonexistent_currency_logging(self):
        currency_list = ['USD', 'KEK']
        captured_output = io.StringIO()
        
        result = get_currencies(currency_list, handle=captured_output)
        
        output = captured_output.getvalue()
        self.assertIn("Код валюты 'KEK' не найден", output)
        self.assertIn('USD', result)
        self.assertNotIn('KEK', result)
        self.assertEqual(len(result), 1) 

    def test_mixed_currencies(self):
        currency_list = ['USD', 'EUR', 'KEK']
        captured_output = io.StringIO()
        
        result = get_currencies(currency_list, handle=captured_output)
        
        output = captured_output.getvalue()
        self.assertIn("Код валюты 'KEK' не найден", output)
        self.assertIn('USD', result)
        self.assertIn('EUR', result)
        self.assertNotIn('KEK', result)
        self.assertEqual(len(result), 2)

unittest.main(verbosity=2)
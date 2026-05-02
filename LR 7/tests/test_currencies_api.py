import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.currencies_api import get_currencies


MAX_REASONABLE_RATE = 1000 


class TestGetCurrencies(unittest.TestCase):

    def test_get_usd(self):
        result = get_currencies(['USD'])

        self.assertIsNotNone(result)
        self.assertIn('USD', result)

        usd = result['USD']

        self.assertIsInstance(usd, dict)
        self.assertIn('value', usd)

        self.assertIsInstance(usd['value'], (int, float))
        self.assertGreater(usd['value'], 0)
        self.assertLess(usd['value'], MAX_REASONABLE_RATE)

    def test_get_multiple(self):
        result = get_currencies(['USD', 'EUR'])

        self.assertIn('USD', result)
        self.assertIn('EUR', result)
        self.assertEqual(len(result), 2)

    def test_nonexistent_currency(self):
        result = get_currencies(['XYZ'])

        self.assertIsInstance(result, dict)
        self.assertEqual(result, {})

    def test_all_currencies(self):
        result = get_currencies()

        self.assertIsInstance(result, dict)
        self.assertGreater(len(result), 10)

    def test_invalid_url(self):
        result = get_currencies(url="https://invalid-url")

        self.assertIsNone(result)


unittest.main(verbosity=2)
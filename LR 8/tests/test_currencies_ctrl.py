import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from unittest.mock import MagicMock
from controllers.currenciesController import CurrenciesController

class TestCurrenciesController(unittest.TestCase):

    def setUp(self):
        self.mock_db = MagicMock()
        self.ctrl = CurrenciesController(self.mock_db)
    

    def test_list_currencies(self):
        self.mock_db._read_currencies.return_value = [
            {'id': 1, 'char_code': 'USD', 'value': 999.9}
        ]

        result = self.ctrl.list_currencies()
        self.assertEqual(result[0]['char_code'], 'USD')
        self.mock_db._read_currencies.assert_called_once()

    def test_delete_currency(self):
        self.ctrl.delete_currency(1)
        self.mock_db._delete_currencies.assert_called_once_with(1)

    def test_update_currency(self):
        self.ctrl.update_currency('USD', 999.9)
        self.mock_db._update_currencies.assert_called_once_with('USD', 999.9)

unittest.main(verbosity=2)
        
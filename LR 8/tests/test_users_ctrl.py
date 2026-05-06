import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from unittest.mock import MagicMock
from controllers.userController import UserController

class TestUsersController(unittest.TestCase):

    def setUp(self):
        self.mock_db = MagicMock()
        self.ctrl = UserController(self.mock_db)

    def test_list_users(self):
        self.mock_db._read_users.return_value = [
            {'id': 1, 'name': 'Heisenberg'}
        ]

        result = self.ctrl.list_users()
        self.assertEqual(result[0]['name'], 'Heisenberg')
        self.mock_db._read_users.assert_called_once()

    def test_get_user(self):
        self.mock_db._get_user.return_value = {'id': 1, 'name': 'Heisenberg'}
        result = self.ctrl.get_user(1)
        self.assertEqual(result['name'], 'Heisenberg')
        self.mock_db._get_user.assert_called_once_with(1)

    def test_get_user_currencies(self):
        self.mock_db._read_user_currencies.return_value = [
            {'id': 1, 'char_code': 'USD', 'value': 999.9}
        ]
        result = self.ctrl.get_user_currencies(1)
        self.assertEqual(result[0]['char_code'], 'USD')
        self.mock_db._read_user_currencies.assert_called_once_with(1)

unittest.main(verbosity=2)
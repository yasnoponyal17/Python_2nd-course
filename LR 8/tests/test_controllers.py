import unittest
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from controllers.currenciesController import currencies
from controllers.userController import users, user
from controllers.authorController import index, author
from models.author import Author
from models.app import App


class TestUsersController(unittest.TestCase):

    def test_users_render(self):
        html = users()

        self.assertIsInstance(html, str)

        self.assertIn("Кто-то", html)
        self.assertIn("Ещё кто-то", html)


class TestUserController(unittest.TestCase):

    def test_user_with_subscriptions(self):
        html = user(1)

        self.assertIsInstance(html, str)

        self.assertIn("Кто-то", html)

        self.assertTrue(
            ("USD" in html) or ("EUR" in html)
        )

    def test_user_second(self):
        html = user(2)

        self.assertIsInstance(html, str)

        self.assertIn("Ещё кто-то", html)

        self.assertTrue(
            ("GBP" in html) or ("JPY" in html)
        )

class TestControllers(unittest.TestCase):

    def setUp(self):
        self.author = Author("Sergei Efimov", "IVT-2")
        self.app = App("Top4ik", "1.3.3.7", self.author)

    def test_index_render(self):
        html = index(self.author, self.app)

        self.assertIsInstance(html, str)

        self.assertIn("Sergei Efimov", html)
        self.assertIn("IVT-2", html)
        self.assertIn("Top4ik", html)

        self.assertIn("Главная", html)
        self.assertIn("/currencies", html)
        self.assertIn("/users", html)

    def test_author_render(self):
        html = author(self.author)

        self.assertIsInstance(html, str)

        self.assertIn("Sergei Efimov", html)
        self.assertIn("IVT-2", html)

unittest.main(verbosity=2)
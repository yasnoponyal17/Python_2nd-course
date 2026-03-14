import unittest
import json
import yaml
from main import Component, JsonDecorator, YamlDecorator, CsvDecorator


class MockComponent(Component):
    def operation(self) -> dict:
        return {"USD": 666.0}

class TestCurrencyDecorators(unittest.TestCase):

    def setUp(self):
        """Этот метод запускается перед каждым тестом"""
        self.source = MockComponent()

    def test_json_decorator(self):
        decorator = JsonDecorator(self.source)
        result = decorator.operation()
        
        data = json.loads(result)
        self.assertEqual(data["USD"], 666.0)
        self.assertIn("USD", data)

    def test_yaml_decorator(self):
        decorator = YamlDecorator(self.source)
        result = decorator.operation()
        
        data = yaml.safe_load(result)
        self.assertEqual(data["USD"], 666.0)

    def test_csv_decorator(self):
        decorator = CsvDecorator(self.source)
        result = decorator.operation()
        
        self.assertIn("Currency,Value", result)
        self.assertIn("USD,666.0", result)


if __name__ == "__main__":
    unittest.main(verbosity=2)
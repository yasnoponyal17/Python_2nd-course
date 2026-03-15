import unittest
import json
import yaml
from main import Component, ConcreteComponent, JsonDecorator, YamlDecorator, CsvDecorator


class MockComponent(Component):
    def operation(self) -> str:
        data = {"USD": 666.0, "EUR": 1337.0}
        return json.dumps(data)

    def save(self, filename: str):
        pass

class TestDecorators(unittest.TestCase):

    def setUp(self):
        self.source = MockComponent()
        
    def test_operation(self):
        source = ConcreteComponent(codes=['USD'])
        result = source.operation()
        self.assertIsInstance(result, str)
        
        data = json.loads(result)
        self.assertIsNotNone(data)

    def test_json_decorator(self):
        decorator = JsonDecorator(self.source)
        result = decorator.operation()
        self.assertIsInstance(result, str)
        
        data = json.loads(result)
        self.assertEqual(data["USD"], 666.0)
        self.assertIn("EUR", data)

    def test_yaml_decorator(self):
        decorator = YamlDecorator(self.source)
        result = decorator.operation()
        
        data = yaml.safe_load(result)
        self.assertEqual(data["USD"], 666.0)
        self.assertIn("EUR", result)

    def test_csv_decorator(self):
        decorator = CsvDecorator(self.source)
        result = decorator.operation()
        
        self.assertIn("Currency,Value", result)
        self.assertIn("USD,666.0", result)


if __name__ == "__main__":
    unittest.main(verbosity=2)
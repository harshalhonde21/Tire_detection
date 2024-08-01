import unittest
from src.model import build_model

class TestModel(unittest.TestCase):
    def test_build_model(self):
        model = build_model()
        self.assertIsNotNone(model)

if __name__ == "__main__":
    unittest.main()

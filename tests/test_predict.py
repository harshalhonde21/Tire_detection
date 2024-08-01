import unittest
from src.predict import predict

class TestPredict(unittest.TestCase):
    def test_predict(self):
        image_path = '../data/raw/example_tire.jpg'
        prediction = predict(image_path)
        self.assertIsInstance(prediction, int)

if __name__ == "__main__":
    unittest.main()

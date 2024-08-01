import unittest
from src.data_preprocessing import load_and_preprocess_data

class TestDataPreprocessing(unittest.TestCase):
    def test_load_and_preprocess_data(self):
        data_dir = '../data/raw'
        X_train, X_test, y_train, y_test = load_and_preprocess_data(data_dir)
        self.assertEqual(len(X_train), len(y_train))
        self.assertEqual(len(X_test), len(y_test))

if __name__ == "__main__":
    unittest.main()

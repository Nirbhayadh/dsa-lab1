from search import binary_search, linear_search
import unittest


class searchTest(unittest.TestCase):
    def test_linear_search(self):
        values = [5, 3, 6, 1, 4, 9, 0]
        result = linear_search(values, 5)
        expected = 0
        self.assertEqual(result, expected)
    def test_binary_search(self):
        values = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
        result = binary_search(values, 22, 0, len(values)-1)
        expected = -1
        self.assertEqual(result, expected)
if __name__ == '__main__':
    unittest.main()


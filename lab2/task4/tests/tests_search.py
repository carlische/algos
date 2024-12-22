import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from search import binary_search
class TestBinarySearch(unittest.TestCase):

    def test_binary_search_found(self):
        array = [1, 2, 3, 4, 5]
        self.assertEqual(binary_search(array, 3), 2)

    def test_binary_search_not_found(self):
        array = [1, 2, 3, 4, 5]
        self.assertEqual(binary_search(array, 6), -1)

    def test_empty_array(self):
        array = []
        self.assertEqual(binary_search(array, 1), -1)

    def test_single_element_found(self):
        array = [55]
        self.assertEqual(binary_search(array, 55), 0)

    def test_single_element_not_found(self):
        array = [55]
        self.assertEqual(binary_search(array, 56), -1)


if __name__ == '__main__':
    unittest.main()
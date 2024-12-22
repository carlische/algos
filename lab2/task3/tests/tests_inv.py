import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from inv import merge_sort_and_count
class TestInversionsCount(unittest.TestCase):

    def test_inversions(self):
        array = [10, 20, 1, 4, 5]
        temp_array = [0] * len(array)
        result = merge_sort_and_count(array, temp_array, 0, len(array) - 1)
        self.assertEqual(result, 6)

    def test_no_inversions(self):
        array = [1, 2, 3, 4, 5]
        temp_array = [0] * len(array)
        result = merge_sort_and_count(array, temp_array, 0, len(array) - 1)
        self.assertEqual(result, 0)

    def test_reverse_sorted(self):
        array = [5, 4, 3, 2, 1]
        temp_array = [0] * len(array)
        result = merge_sort_and_count(array, temp_array, 0, len(array) - 1)
        self.assertEqual(result, 10)

    def test_empty_array(self):
        array = []
        temp_array = []
        result = merge_sort_and_count(array, temp_array, 0, len(array) - 1)
        self.assertEqual(result, 0)



if __name__ == '__main__':
    unittest.main()
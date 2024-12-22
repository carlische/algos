import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from merge_sort_i import merge_sort_with_indices
class TestMergeSort(unittest.TestCase):

    def test_basic_sort(self):
        array = [2, 11, 4, 2, 100, 1]
        merge_sort_with_indices(array, 0, len(array) - 1)
        self.assertEqual(array, [1, 2, 2, 4, 11, 100])

    def test_already_sorted(self):
        array = [1, 2, 3, 4, 5, 6, 7, 8]
        merge_sort_with_indices(array, 0, len(array) - 1)
        self.assertEqual(array, [1, 2, 3, 4, 5, 6, 7, 8])

    def test_reverse_sorted(self):
        array = [8, 7, 6, 5, 4, 3, 2, 1]
        merge_sort_with_indices(array, 0, len(array) - 1)
        self.assertEqual(array, [1, 2, 3, 4, 5, 6, 7, 8])

    def test_single_element(self):
        array = [100]
        merge_sort_with_indices(array, 0, len(array) - 1)
        self.assertEqual(array, [100])

    def test_empty_array(self):
        array = []
        merge_sort_with_indices(array, 0, len(array) - 1)
        self.assertEqual(array, [])

    def test_large_numbers(self):
        array = [1000000000, 999999999, 999999998]
        merge_sort_with_indices(array, 0, len(array) - 1)
        self.assertEqual(array, [999999998, 999999999, 1000000000])

if __name__ == '__main__':
    unittest.main()
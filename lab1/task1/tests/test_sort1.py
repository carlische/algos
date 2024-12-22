import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from sort1 import insertion_sort


class TestInsertionSort(unittest.TestCase):
    """
    Набор тестов для функции сортировки вставками.
    """

    def test_sorted_array(self):
        """
        Проверка работы на уже отсортированном массиве.
        """
        self.assertEqual(insertion_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_reverse_sorted_array(self):
        """
        Проверка работы на массиве, отсортированном в обратном порядке.
        """
        self.assertEqual(insertion_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

    def test_unsorted_array(self):
        """
        Проверка работы на случайном неотсортированном массиве.
        """
        self.assertEqual(insertion_sort([31, 41, 59, 26, 41, 58]), [26, 31, 41, 41, 58, 59])

    def test_array_with_duplicates(self):
        """
        Проверка работы на массиве с дубликатами.
        """
        self.assertEqual(insertion_sort([2, 3, 2, 3, 1]), [1, 2, 2, 3, 3])

    def test_single_element_array(self):
        """
        Проверка работы на массиве с одним элементом.
        """
        self.assertEqual(insertion_sort([42]), [42])

    def test_empty_array(self):
        """
        Проверка работы на пустом массиве.
        """
        self.assertEqual(insertion_sort([]), [])

if __name__ == '__main__':
    unittest.main()
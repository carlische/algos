import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from sort5 import s_sort


class TestSelectionSort(unittest.TestCase):
    """
    Набор тестов для функции сортировки выбором.
    """

    def test_basic_case(self):
        """
        Проверка корректной сортировки на обычном массиве.
        """
        self.assertEqual(s_sort([31, 41, 59, 26, 41, 58]), [26, 31, 41, 41, 58, 59])

    def test_sorted_array(self):
        """
        Проверка корректности работы на уже отсортированном массиве.
        """
        self.assertEqual(s_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_reverse_sorted_array(self):
        """
        Проверка корректности работы на массиве, отсортированном в обратном порядке.
        """
        self.assertEqual(s_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

    def test_array_with_duplicates(self):
        """
        Проверка корректной работы на массиве с дубликатами.
        """
        self.assertEqual(s_sort([3, 3, 2, 1, 3]), [1, 2, 3, 3, 3])

    def test_single_element(self):
        """
        Проверка корректности работы на массиве с одним элементом.
        """
        self.assertEqual(s_sort([42]), [42])

    def test_empty_array(self):
        """
        Проверка корректной работы на пустом массиве.
        """
        self.assertEqual(s_sort([]), [])


if __name__ == '__main__':
    unittest.main()
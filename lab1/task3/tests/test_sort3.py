import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from sort3 import insertion_sort


class TestInsertionSortDescending(unittest.TestCase):
    """
    Набор тестов для функции сортировки вставками по убыванию.
    """

    def test_basic_case(self):
        """
        Проверка корректной сортировки по убыванию на обычном случае.
        """
        self.assertEqual(insertion_sort([4, 3, 2, 1]), [4, 3, 2, 1])
        self.assertEqual(insertion_sort([1, 2, 3, 4]), [4, 3, 2, 1])

    def test_with_duplicates(self):
        """
        Проверка корректной сортировки при наличии дубликатов в массиве.
        """
        self.assertEqual(insertion_sort([3, 3, 1, 2, 3]), [3, 3, 3, 2, 1])

    def test_single_element(self):
        """
        Проверка корректности работы на массиве с одним элементом.
        """
        self.assertEqual(insertion_sort([42]), [42])

    def test_empty_array(self):
        """
        Проверка работы на пустом массиве.
        """
        self.assertEqual(insertion_sort([]), [])

if __name__ == '__main__':
    unittest.main()
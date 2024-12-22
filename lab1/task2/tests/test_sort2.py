import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from sort2 import insertion_sort

class TestInsertionSortWithIndices(unittest.TestCase):
    """
    Набор тестов для функции сортировки вставками с отслеживанием перемещений элементов.
    """

    def test_basic_case(self):
        """
        Проверка корректной сортировки и возвращаемых индексов при обычном случае.
        """
        indexes, sorted_array = insertion_sort([4, 3, 2, 1])
        self.assertEqual(sorted_array, [1, 2, 3, 4])
        self.assertEqual(indexes, [0, 1, 2, 3])

    def test_with_duplicates(self):
        """
        Проверка корректной сортировки и возвращаемых индексов при наличии дубликатов в массиве.
        """
        indexes, sorted_array = insertion_sort([3, 3, 1, 2, 3])
        self.assertEqual(sorted_array, [1, 2, 3, 3, 3])
        self.assertEqual(indexes, [0, 1, 2, 3, 4])

    def test_sorted_array(self):
        """
        Проверка корректности работы на уже отсортированном массиве.
        """
        indexes, sorted_array = insertion_sort([1, 2, 3, 4, 5])
        self.assertEqual(sorted_array, [1, 2, 3, 4, 5])
        self.assertEqual(indexes, [0, 1, 2, 3, 4])

    def test_single_element(self):
        """
        Проверка корректности работы на массиве с одним элементом.
        """
        indexes, sorted_array = insertion_sort([42])
        self.assertEqual(sorted_array, [42])
        self.assertEqual(indexes, [0])

    def test_empty_array(self):
        """
        Проверка работы на пустом массиве.
        """
        indexes, sorted_array = insertion_sort([])
        self.assertEqual(sorted_array, [])
        self.assertEqual(indexes, [0])

if __name__ == '__main__':
    unittest.main()


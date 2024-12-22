import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from sort4 import l_search


class TestLinearSearch(unittest.TestCase):
    """
    Набор тестов для функции линейного поиска.
    """

    def test_element_found(self):
        """
        Проверка корректного поиска элемента, который присутствует в массиве.
        """
        self.assertEqual(l_search(['10', '20', '30', '40'], '30'), ['2'])

    def test_element_not_found(self):
        """
        Проверка корректной обработки случая, когда элемент отсутствует в массиве.
        """
        self.assertEqual(l_search(['10', '20', '30', '40'], '50'), '-1')

    def test_multiple_occurrences(self):
        """
        Проверка корректного поиска элемента, который встречается несколько раз в массиве.
        """
        self.assertEqual(l_search(['10', '20', '30', '30', '40'], '30'), ['2', '3'])

    def test_single_element_found(self):
        """
        Проверка корректности работы на массиве с одним элементом, который совпадает с искомым.
        """
        self.assertEqual(l_search(['42'], '42'), ['0'])

    def test_single_element_not_found(self):
        """
        Проверка корректности работы на массиве с одним элементом, который не совпадает с искомым.
        """
        self.assertEqual(l_search(['42'], '43'), '-1')

    def test_empty_array(self):
        """
        Проверка корректной работы на пустом массиве.
        """
        self.assertEqual(l_search([], '10'), '-1')


if __name__ == '__main__':
    unittest.main()
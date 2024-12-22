import unittest
from utils import memory_data, time_data
from lab3.task1.src.quick_sort import quick_sort, main
from utils import generate_random_array


class TestQuickSort(unittest.TestCase):

    def test_should_sort_example_array(self):
        # given
        n = 5
        array = [2, 3, 9, 2, 2]
        expected_result = [2, 2, 2, 3, 9]

        # when
        result = quick_sort(array, 0, n - 1)

        # then
        self.assertEqual(result, expected_result)

    def test_should_sort_sorted_array(self):
        # given
        n = 6
        array = [1, 2, 3, 4, 5, 6]
        expected_result = [1, 2, 3, 4, 5, 6]

        # when
        result = quick_sort(array, 0, n - 1)

        # then
        self.assertEqual(result, expected_result)

    def test_should_sort_reverse_sorted_array(self):
        # given
        n = 6
        array = [6, 5, 4, 3, 2, 1]
        expected_result = [1, 2, 3, 4, 5, 6]

        # when
        result = quick_sort(array, 0, n - 1)

        # then
        self.assertEqual(result, expected_result)

    def test_should_sort_single_element_array(self):
        # given
        n = 1
        array = [0]
        expected_result = [0]

        # when
        result = quick_sort(array, 0,n - 1)

        # then
        self.assertEqual(result, expected_result)

    def test_should_sort_empty_array(self):
        # given
        n = 0
        array = []
        expected_result = []

        # when
        result = quick_sort(array, 0, len(array) - 1)

        # then
        self.assertEqual(result, expected_result)

    def test_should_sort_large_numbers_array(self):
        # given
        n = 10**5
        array = generate_random_array(n, -10**9, 10**9)
        expected_result = sorted(array)

        # when
        result = quick_sort(array, 0, n - 1)

        # then
        self.assertEqual(result, expected_result)

    def test_should_check_time_data(self):
        # given
        expected_time = 2

        # when
        time = time_data(main)

        # then
        self.assertLess(time, expected_time)

    def test_should_check_memory_data(self):
        # given
        expected_memory = 256

        # when
        current, peak = memory_data(main)

        # then
        self.assertLess(current, expected_memory)
        self.assertLess(peak, expected_memory)


if __name__ == '__main__':
    unittest.main()

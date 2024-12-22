import unittest
from utils import memory_data, time_data
from lab3.task6.src.sum_of_tenths import sum_of_tenths, main


class TestSumOfTenths(unittest.TestCase):

    def test_should_count_sum_of_tenths_example_array(self):
        # given
        A = [7, 1, 4, 9]
        B = [2, 7, 8, 11]
        expected_result = 51

        # when
        result = sum_of_tenths(A, B)

        # then
        self.assertEqual(result, expected_result)

    def test_should_count_sum_of_tenths_sorted_array(self):
        # given
        A = [1, 2, 3, 4, 5]
        B = [1, 1, 1, 1, 1]
        expected_result = 9

        # when
        result = sum_of_tenths(A, B)

        # then
        self.assertEqual(result, expected_result)

    def test_should_count_sum_of_tenths_reverse_sorted_array(self):
        # given
        A = [5, 4, 3, 2, 1]
        B = [1, 2, 3, 4, 5]
        expected_result = 22

        # when
        result = sum_of_tenths(A, B)

        # then
        self.assertEqual(result, expected_result)

    def test_should_count_sum_of_tenths_empty_array(self):
        # given
        A = []
        B = []
        expected_result = 0

        # when
        result = sum_of_tenths(A, B)

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

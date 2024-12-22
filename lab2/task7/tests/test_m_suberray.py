import unittest
from lab2.task7.utils import memory_data, time_data
from lab2.task7.src.m_suberray import find_max_subarray, main


class TestFindMaxSubarray(unittest.TestCase):

    def test_should_find_max_subarray_example_array(self):
        # given
        n = 4
        array = [1, 8, 2, 10]
        expected_result = [21, [0, 3]]

        # when
        result = find_max_subarray(n, array)

        # then
        self.assertEqual(result, expected_result)

    def test_should_find_max_subarray_single_element_array(self):
        # given
        n = 1
        array = [1]
        expected_result = [1, [0, 0]]

        # when
        result = find_max_subarray(n, array)

        # then
        self.assertEqual(result, expected_result)

    def test_should_find_max_subarray_empty_array(self):
        # given
        n = 0
        array = []
        expected_result = [0, [0, 0]]

        # when
        result = find_max_subarray(n, array)

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

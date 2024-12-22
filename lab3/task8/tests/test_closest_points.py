import unittest
from utils import memory_data, time_data
from lab3.task8.src.closest_points import closest_points, main


class TestClosestPoints(unittest.TestCase):

    def test_should_find_closest_points_example1_array(self):
        # given
        k = 1
        array = [[1, 3], [-2, 2]]
        expected_result = [[-2, 2]]

        # when
        result = closest_points(array, k)

        # then
        self.assertEqual(result, expected_result)

    def test_should_find_closest_points_example2_array(self):
        # given
        k = 2
        array = [[3, 3], [5, -1], [-2, 4]]
        expected_result = [[3, 3], [-2, 4]]

        # when
        result = closest_points(array, k)

        # then
        self.assertEqual(result, expected_result)

    def test_should_find_closest_points_sorted_array(self):
        # given
        k = 2
        array = [[1, 1], [-2, 2], [4, -3], [-7, -4]]
        expected_result = [[1, 1], [-2, 2]]

        # when
        result = closest_points(array, k)

        # then
        self.assertEqual(result, expected_result)

    def test_should_find_closest_points_reverse_sorted_array(self):
        # given
        k = 2
        array = [[-7, -4], [4, -3], [-2, 2], [1, 1]]
        expected_result = [[1, 1], [-2, 2]]

        # when
        result = closest_points(array, k)

        # then
        self.assertEqual(result, expected_result)

    def test_should_find_closest_points_empty_array(self):
        # given
        k = 4
        array = []
        expected_result = []

        # when
        result = closest_points(array, k)

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

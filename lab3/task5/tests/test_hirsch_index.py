import unittest
from utils import memory_data, time_data
from lab3.task5.src.hirsch_index import hirsch_index, main


class TestHirschIndex(unittest.TestCase):

    def test_should_find_hirsch_index_example1_array(self):
        # given
        array = [3, 0, 6, 1, 5]
        expected_result = 3

        # when
        result = hirsch_index(array)

        # then
        self.assertEqual(result, expected_result)

    def test_should_find_hirsch_index_example2_array(self):
        # given
        array = [1, 3, 1]
        expected_result = 1

        # when
        result = hirsch_index(array)

        # then
        self.assertEqual(result, expected_result)

    def test_should_find_hirsch_index_sorted_array(self):
        # given
        array = [1, 2, 3, 4]
        expected_result = 2

        # when
        result = hirsch_index(array)

        # then
        self.assertEqual(result, expected_result)

    def test_should_find_hirsch_index_reverse_sorted_array(self):
        # given
        array = [4, 3, 2, 1]
        expected_result = 2

        # when
        result = hirsch_index(array)

        # then
        self.assertEqual(result, expected_result)

    def test_should_count_inversions_empty_array(self):
        # given
        array = []
        expected_result = 0

        # when
        result = hirsch_index(array)

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

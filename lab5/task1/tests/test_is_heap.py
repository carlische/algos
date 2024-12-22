import unittest
from utils import memory_data, time_data
from lab5.task1.src.is_heap import main, is_heap


class TestIsHeap(unittest.TestCase):

    def test_should_check_incorrect_data(self):
        # given
        n = 5
        data = [1, 0, 1, 2, 0]
        expected_result = 'NO'

        # when
        result = is_heap(n, data)

        # then
        self.assertEqual(result, expected_result)

    def test_should_check_correct_data(self):
        # given
        n = 5
        data = [1, 3, 2, 5, 4]
        expected_result = 'YES'

        # when
        result = is_heap(n, data)

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


if __name__ == "__main__":
    unittest.main()

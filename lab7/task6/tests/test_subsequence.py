import unittest
from utils import memory_data, time_data
from lab7.task6.src.subsequence import main, subsequence


class TestSubsequence(unittest.TestCase):

    def test_should_work_with_small_input(self):
        # given
        n = 6
        array = [3, 29, 5, 5, 28, 6]
        expected_result = ([3], [3, 5, 6])

        # when
        result = subsequence(n, array)

        # then
        self.assertEqual(result, expected_result)

    def test_should_work_when_all_equal_elements(self):
        # given
        n = 5
        sequence = [7, 7, 7, 7, 7]
        exp_length = [1]
        exp_sequence = [7]

        # when
        length, sequence = subsequence(n, sequence)

        # then
        self.assertEqual(length, exp_length)
        self.assertEqual(sequence, exp_sequence)

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

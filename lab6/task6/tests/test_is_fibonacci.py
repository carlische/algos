import unittest
from utils import memory_data, time_data
from lab6.task6.src.is_fibonacci import main, is_fibonacci


class TestFibonacci(unittest.TestCase):

    def test_should_recognize_fibonacci_numbers(self):
        # given
        numbers = [0, 1, 8, 21]
        expected_results = ['Yes', 'Yes', 'Yes', 'Yes']

        # when
        results = [is_fibonacci(n) for n in numbers]

        # then
        self.assertEqual(results, expected_results)

    def test_should_check_large_fibonacci_numbers(self):
        # given
        large_numbers = [144, 987, 1597, 2584]
        expected_results = ['Yes', 'Yes', 'Yes', 'Yes']

        # when
        results = [is_fibonacci(n) for n in large_numbers]

        # then
        self.assertEqual(results, expected_results)

    def test_should_check_non_fibonacci_numbers(self):
        # given
        non_fibonacci_numbers = [13, 30, 55, 89]
        expected_results = ['Yes', 'No', 'Yes', 'Yes']

        # when
        results = [is_fibonacci(n) for n in non_fibonacci_numbers]

        # then
        self.assertEqual(results, expected_results)

    def test_should_check_time_data(self):
        # given
        expected_time = 2

        # when
        time = time_data(main)

        # then
        self.assertLess(time, expected_time)

    def test_should_check_memory_data(self):
        # given
        expected_memory = 128

        # when
        current, peak = memory_data(main)

        # then
        self.assertLess(current, expected_memory)
        self.assertLess(peak, expected_memory)


if __name__ == "__main__":
    unittest.main()

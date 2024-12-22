import unittest
from utils import memory_data, time_data
from lab7.task2.src.primitive_calculator import main, primitive_calculator


class TestPrimitiveCalculator(unittest.TestCase):

    def test_should_work_for_small_input(self):
        # given
        n = 6
        expected_output = ([2], [1, 2, 6])

        # when
        result = primitive_calculator(n)

        # then
        self.assertEqual(result, expected_output)

    def test_should_work_for_large_input(self):
        # given
        n = 96234
        expected_output = ([14], [1, 3, 9, 10, 11, 22, 66, 198, 594, 1782, 5346, 16038, 16039, 32078, 96234])

        # when
        result = primitive_calculator(n)

        # then
        self.assertEqual(result, expected_output)

    def test_should_check_time_data(self):
        # given
        expected_time = 1

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
        self. assertLess(peak, expected_memory)


if __name__ == "__main__":
    unittest.main()

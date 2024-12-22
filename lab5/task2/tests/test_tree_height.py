import unittest
from utils import memory_data, time_data
from lab5.task2.src.tree_height import main, tree_height


class TestTreeHeight(unittest.TestCase):

    def test_should_check_example1_data(self):
        # given
        n = 5
        data = [4, -1, 4, 1, 1]
        expected_result = 3

        # when
        result = tree_height(n, data)

        # then
        self.assertEqual(result, expected_result)

    def test_should_check_example2_data(self):
        # given
        n = 5
        data = [-1, 0, 4, 0, 3]
        expected_result = 4

        # when
        result = tree_height(n, data)

        # then
        self.assertEqual(result, expected_result)

    def test_should_check_time_data(self):
        # given
        expected_time = 3

        # when
        time = time_data(main)

        # then
        self.assertLess(time, expected_time)

    def test_should_check_memory_data(self):
        # given
        expected_memory = 512

        # when
        current, peak = memory_data(main)

        # then
        self.assertLess(current, expected_memory)
        self.assertLess(peak, expected_memory)


if __name__ == "__main__":
    unittest.main()

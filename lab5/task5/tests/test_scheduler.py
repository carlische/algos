import unittest
from utils import memory_data, time_data
from lab5.task5.src.scheduler import main, scheduler


class TestScheduler(unittest.TestCase):

    def test_should_check_example1_data(self):
        # given
        n, m = 2, 5
        data = [1, 2, 3, 4, 5]
        expected_result = [(0, 0), (1, 0), (0, 1), (1, 2), (0, 4)]

        # when
        result = scheduler(n, data)

        # then
        self.assertEqual(result, expected_result)

    def test_should_check_example2_data(self):
        # given
        n, m = 4, 20
        data = [1] * 20
        expected_result = [(0, 0), (1, 0), (2, 0), (3, 0), (0, 1), (1, 1), (2, 1), (3, 1), (0, 2), (1, 2), (2, 2), (3, 2), (0, 3), (1, 3), (2, 3), (3, 3), (0, 4), (1, 4), (2, 4), (3, 4)]

        # when
        result = scheduler(n, data)

        # then
        self.assertEqual(result, expected_result)

    def test_should_check_empty_data(self):
        # given
        n = 4
        data = []
        expected_result = []

        # when
        result = scheduler(n, data)

        # then
        self.assertEqual(result, expected_result)

    def test_should_check_one_task_data(self):
        # given
        n = 2
        data = [5]
        expected_result = [(0, 0)]

        # when
        result = scheduler(n, data)

        # then
        self.assertEqual(result, expected_result)

    def test_should_check_time_data(self):
        # given
        expected_time = 6

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

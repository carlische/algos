import unittest
from utils import memory_data, time_data
from lab4.task6.src.queue_with_min import main, QueueWithMin


class TestQueueWithMin(unittest.TestCase):
    def setUp(self) -> None:
        self.queue = QueueWithMin()
        
    def test_should_check_get_min(self):
        # given
        self.queue.push(10)
        expected_result = 10

        # when
        result = self.queue.get_min()

        # then
        self.assertEqual(result, expected_result)

    def test_should_check_get_min_and_pop(self):
        # given
        self.queue.push(10)
        self.queue.push(20)

        # when (удалили число 10 - текущий минимум)
        self.queue.pop()

        # then
        self.assertEqual(self.queue.get_min(), 20)

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

import unittest
from utils import memory_data, time_data
from lab4.task9.src.polyclinic import main, Queue


class TestPolyclinic(unittest.TestCase):
    
    def setUp(self) -> None:
        self.queue = Queue()

    def test_should_check_length_initial(self):
        # given
        expected_len = 0

        # when
        queue_len = len(self.queue)

        # then
        self.assertEqual(queue_len, expected_len)

    def test_should_check_push_to_end(self):
        # when (step 1)
        self.queue.push_to_end(10)

        # then
        self.assertEqual(len(self.queue), 1)
        self.assertEqual(self.queue.head.value, 10)
        self.assertEqual(self.queue.middle.value, 10)
        self.assertEqual(self.queue.end.value, 10)

        # when (step 2)
        self.queue.push_to_end(20)

        # then
        self.assertEqual(len(self.queue), 2)
        self.assertEqual(self.queue.head.value, 10)
        self.assertEqual(self.queue.middle.value, 10)
        self.assertEqual(self.queue.end.value, 20)

        # when (step 3)
        self.queue.push_to_end(30)

        # then
        self.assertEqual(len(self.queue), 3)
        self.assertEqual(self.queue.head.value, 10)
        self.assertEqual(self.queue.middle.value, 20)
        self.assertEqual(self.queue.end.value, 30)

    def test_should_check_push_to_middle(self):
        # given
        self.queue.push_to_end(10)
        self.queue.push_to_end(20)
        self.queue.push_to_end(40)
        self.queue.push_to_end(50)

        # when (step 1)
        self.queue.push_to_middle(30)

        # then
        self.assertEqual(len(self.queue), 5)
        self.assertEqual(self.queue.head.value, 10)
        self.assertEqual(self.queue.middle.value, 30)
        self.assertEqual(self.queue.end.value, 50)

        # when (step 2)
        self.queue.push_to_middle(31)

        # then
        self.assertEqual(len(self.queue), 6)
        self.assertEqual(self.queue.head.value, 10)
        self.assertEqual(self.queue.middle.value, 30)
        self.assertEqual(self.queue.middle.next.value, 31)
        self.assertEqual(self.queue.end.value, 50)

    def test_should_check_pop_from_head(self):
        # given
        self.queue.push_to_end(10)
        self.queue.push_to_end(20)
        self.queue.push_to_end(30)

        # when (step 1)
        self.assertEqual(self.queue.pop_from_head(), 10)

        # then
        self.assertEqual(len(self.queue), 2)
        self.assertEqual(self.queue.head.value, 20)
        self.assertEqual(self.queue.middle.value, 20)
        self.assertEqual(self.queue.end.value, 30)

        # when (step 2)
        self.assertEqual(self.queue.pop_from_head(), 20)

        # then
        self.assertEqual(len(self.queue), 1)
        self.assertEqual(self.queue.head.value, 30)
        self.assertEqual(self.queue.middle.value, 30)
        self.assertEqual(self.queue.end.value, 30)

        # when (step 3)
        self.assertEqual(self.queue.pop_from_head(), 30)

        # then
        self.assertEqual(len(self.queue), 0)
        self.assertIsNone(self.queue.head)
        self.assertIsNone(self.queue.middle)
        self.assertIsNone(self.queue.end)

    def test_should_check_pop_from_empty_queue(self):
        with self.assertRaises(IndexError):
            self.queue.pop_from_head()

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

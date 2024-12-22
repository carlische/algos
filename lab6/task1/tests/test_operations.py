import unittest
from utils import memory_data, time_data
from lab6.task1.src.operations import main, operations


class TestOperations(unittest.TestCase):

    def test_should_add_and_query_element(self):
        # given
        data = [
            ('A', 1),
            ('?', 1),
            ('D', 1),
            ('?', 1)
        ]
        expected_result = ['Y', 'N']

        # when
        result = operations(data)

        # then
        self.assertEqual(result, expected_result)

    def test_should_handle_multiple_elements(self):
        # given
        data = [
            ('A', 1),
            ('A', 2),
            ('A', 3),
            ('?', 1),
            ('?', 2),
            ('?', 3),
            ('D', 2),
            ('?', 2),
            ('?', 3)
        ]
        expected_result = ['Y', 'Y', 'Y', 'N', 'Y']

        # when
        result = operations(data)

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

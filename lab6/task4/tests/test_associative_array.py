import unittest
from utils import memory_data, time_data
from lab6.task4.src.associative_array import main, associative_array


class TestAssociativeArray(unittest.TestCase):

    def test_should_put_and_get_values(self):
        # given
        commands = [
            ["put", "key1", "value1"],
            ["get", "key1"],
            ["put", "key1", "new_value1"],
            ["get", "key1"]
        ]
        expected_results = ["value1", "new_value1"]

        # when
        results = associative_array(commands)

        # then
        self.assertEqual(results, expected_results)

    def test_should_find_previous_and_next_elements(self):
        # given
        commands = [
            ["put", "key1", "value1"],
            ["put", "key2", "value2"],
            ["put", "key3", "value3"],
            ["prev", "key2"],
            ["next", "key2"]
        ]
        expected_results = ["value1", "value3"]

        # when
        results = associative_array(commands)

        # then
        self.assertEqual(results, expected_results)

    def test_should_delete_key_and_check_its_absence(self):
        # given
        commands = [
            ["put", "key1", "value1"],
            ["put", "key2", "value2"],
            ["delete", "key1"],
            ["get", "key1"],
            ["get", "key2"]
        ]
        expected_results = ["<none>", "value2"]

        # when
        results = associative_array(commands)

        # then
        self.assertEqual(results, expected_results)

    def test_should_check_time_data(self):
        # given
        expected_time = 4

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

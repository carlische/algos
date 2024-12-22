import unittest
from utils import memory_data, time_data
from lab6.task2.src.phone_book import main, phone_book


class TestPhoneBook(unittest.TestCase):

    def test_should_add_and_find_number(self):
        # given
        data = [
            ["add", "911", "police"],
            ["find", "911"]
        ]
        expected_result = ["police"]

        # when
        result = phone_book(data)

        # then
        self.assertEqual(result, expected_result)

    def test_should_delete_and_find_number(self):
        # given
        data = [
            ["add", "1234567890", "John Doe"],
            ["del", "1234567890"],
            ["find", "1234567890"]
        ]
        expected_result = ["not found"]

        # when
        result = phone_book(data)

        # then
        self.assertEqual(result, expected_result)

    def test_should_handle_multiple_commands(self):
        # given
        data = [
            ["add", "911", "police"],
            ["add", "112", "ambulance"],
            ["find", "911"],
            ["find", "112"],
            ["del", "112"],
            ["find", "112"]
        ]
        expected_result = ["police", "ambulance", "not found"]

        # when
        result = phone_book(data)

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

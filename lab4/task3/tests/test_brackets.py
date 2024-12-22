import unittest
from utils import memory_data, time_data
from lab4.task3.src.brackets import main, brackets_check


class TestBrackets(unittest.TestCase):

    def test_should_check_correct_data(self):
        # given
        data = ['()()', '([])', '[([]())]', '']

        # when
        res0 = brackets_check(data[0])
        res1 = brackets_check(data[1])
        res2 = brackets_check(data[2])
        res3 = brackets_check(data[3])

        # then
        self.assertIs(res0, True)
        self.assertIs(res1, True)
        self.assertIs(res2, True)
        self.assertIs(res3, True)

    def test_should_check_incorrect_data(self):
        # given
        data = ['([)]', '((]]', ')(']

        # when
        res0 = brackets_check(data[0])
        res1 = brackets_check(data[1])
        res2 = brackets_check(data[2])

        # then
        self.assertIs(res0, False)
        self.assertIs(res1, False)
        self.assertIs(res2, False)

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

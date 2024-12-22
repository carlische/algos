import unittest
from utils import memory_data, time_data
from lab7.task7.src.patterns import main, patterns


class TestPatternMatching(unittest.TestCase):

    def test_should_match_pattern(self):
        # given
        pattern = "ab*"
        string = "aba"
        expected_result = 'YES'

        # when
        result = patterns(pattern, string)

        # then
        self.assertEqual(result, expected_result)

    def test_should_not_match_pattern(self):
        # given
        pattern = "a*b*c"
        string = "abc"
        expected_result = 'YES'

        # when
        result = patterns(pattern, string)

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

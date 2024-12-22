import unittest
from utils import memory_data, time_data
from lab4.task8.src.postfix_notation import main, postfix_notation


class TestPostfixNotation(unittest.TestCase):
    def test_should_check_addition(self):
        # given
        expression = ['18', '21', '+']
        expected_result = 39

        # when
        result = postfix_notation(expression)

        # then
        self.assertEqual(result, expected_result)

    def test_should_check_multiplication(self):
        # given
        expression = ['10', '2', '*']
        expected_result = 20

        # when
        result = postfix_notation(expression)

        # then
        self.assertEqual(result, expected_result)

    def test_should_check_subtraction(self):
        # given
        expression = ['57', '14', '-']
        expected_result = 43

        # when
        result = postfix_notation(expression)

        # then
        self.assertEqual(result, expected_result)

    def test_should_check_complex_expression(self):
        # given
        expression = ['8', '9', '+', '1', '7', '-', '*']
        expected_result = -102

        # when
        result = postfix_notation(expression)

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

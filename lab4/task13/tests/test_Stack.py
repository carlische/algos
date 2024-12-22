import unittest
from lab4.task13.src.stack import Stack


class TestStack(unittest.TestCase):

    def setUp(self):
        self.stack = Stack()

    def test_should_check_push(self):
        # given
        expected_len = 3

        # when
        self.stack.push(1)
        self.stack.push(2)
        self.stack.push(3)

        result = len(self.stack.stack)

        # then
        self.assertEqual(result, expected_len)

    def test_should_check_is_empty(self):
        self.assertTrue(self.stack.is_empty())

        # when
        self.stack.push(1)

        # then
        self.assertFalse(self.stack.is_empty())

    def test_should_check_deleted_items(self):
        # given
        self.stack.push(1)
        self.stack.push(2)
        expected_result = 2

        # when
        result = self.stack.pop()

        # then
        self.assertEqual(result, expected_result)

    def test_should_check_pop(self):
        # given
        self.stack.push(1)
        self.stack.push(2)

        # when
        self.stack.pop()
        self.stack.pop()

        # then
        self.assertTrue(self.stack.is_empty())

    def test_should_check_pop_from_empty_stack(self):
        with self.assertRaises(IndexError):
            self.stack.pop()

    def test_should_check_len(self):
        self.assertTrue(self.stack.is_empty())

        # when (step 1)
        self.stack.push(5)

        # then
        self.assertEqual(len(self.stack.stack), 1)

        # when (step 2)
        self.stack.pop()

        # then
        self.assertTrue(self.stack.is_empty())


if __name__ == '__main__':
    unittest.main()

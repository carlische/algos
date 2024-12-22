import unittest
from lab4.task13.src.singly_linked_list import SinglyLinkedList


class TestSinglyLinkedList(unittest.TestCase):
    def setUp(self):
        self.linked_list = SinglyLinkedList()

    def test_should_check_initialization(self):
        self.assertEqual(len(self.linked_list), 0)
        self.assertIsNone(self.linked_list.head)

    def test_should_check_push(self):
        # when (step 1)
        self.linked_list.push(10)

        # then
        self.assertEqual(len(self.linked_list), 1)
        self.assertEqual(self.linked_list.head.value, 10)

        # when (step 2)
        self.linked_list.push(20)

        # then
        self.assertEqual(len(self.linked_list), 2)
        self.assertEqual(self.linked_list.head.value, 20)

    def test_should_check_pop(self):
        # given
        with self.assertRaises(IndexError):
            self.linked_list.pop()

        self.linked_list.push(10)
        self.linked_list.push(20)
        self.linked_list.push(30)

        # when (step 1)
        self.assertEqual(self.linked_list.pop(), 30)

        # then
        self.assertEqual(len(self.linked_list), 2)

        # when (step 2)
        self.assertEqual(self.linked_list.pop(), 20)

        # then
        self.assertEqual(len(self.linked_list), 1)

        # when (step 3)
        self.assertEqual(self.linked_list.pop(), 10)

        # then
        self.assertEqual(len(self.linked_list), 0)

    def test_should_check_find(self):
        # given
        self.linked_list.push(10)
        self.linked_list.push(20)
        self.linked_list.push(30)

        # when
        result = self.linked_list.find(20)

        # then
        self.assertIsNotNone(result)
        self.assertEqual(self.linked_list.find(20).value, 20)

    def test_should_check_remove_after(self):
        # given
        self.linked_list.push(10)
        self.linked_list.push(20)
        self.linked_list.push(30)

        # when
        result = self.linked_list.remove_after(30)

        # then
        self.assertEqual(result, 20)


if __name__ == '__main__':
    unittest.main()

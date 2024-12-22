import unittest
from utils import memory_data, time_data
from lab3.task2.src.anti_quick_sort import anti_quick_sort, main


class TestAntiQuickSort(unittest.TestCase):

    def test_should_create_check_permutation_of_n_nums(self):
        # given
        # example n
        n1 = 3
        expected_result1 = [1, 3, 2]

        # another average n
        n2 = 10
        expected_result2 = [1, 4, 6, 8, 10, 5, 3, 7, 2, 9]

        # when
        result1 = anti_quick_sort(n1)
        result2 = anti_quick_sort(n2)

        # then
        self.assertEqual(result1, expected_result1)
        self.assertEqual(result2, expected_result2)

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


if __name__ == '__main__':
    unittest.main()

import unittest
from utils import memory_data, time_data
from lab7.task1.src.coin_exchange import main, coin_exchange


class TestCoinExchange(unittest.TestCase):

    def test_should_work_with_small_amount_of_money(self):
        # given
        money = 6
        coins = [1, 3, 4]
        expected_result = 2

        # when
        result = coin_exchange(money, coins)

        # then
        self.assertEqual(result, expected_result)

    def test_should_work_with_large_amount_of_money(self):
        # given
        money = 10000
        coins = [100, 200, 400]
        expected_result = 25

        # when
        result = coin_exchange(money, coins)

        # then
        self.assertEqual(result, expected_result)

    def test_should_check_time_data(self):
        # given
        expected_time = 1

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

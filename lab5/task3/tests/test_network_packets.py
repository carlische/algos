import unittest
from utils import memory_data, time_data
from lab5.task3.src.network_packets import main, network_packets


class TestNetworkPackets(unittest.TestCase):

    def test_should_check_empty_data(self):
        # given
        s, n = 1, 0
        data = []
        expected_result = None

        # when
        result = network_packets(s, n, data)

        # then
        self.assertEqual(result, expected_result)

    def test_should_check_example2_data(self):
        # given
        s, n = 1, 1
        data = [(0, 0)]
        expected_result = [0]

        # when
        result = network_packets(s, n, data)

        # then
        self.assertEqual(result, expected_result)

    def test_should_check_example13_data(self):
        # given
        s, n = 2, 3
        data = [(0, 1), (3, 1), (10, 1)]
        expected_result = [0, 3, 10]

        # when
        result = network_packets(s, n, data)

        # then
        self.assertEqual(result, expected_result)

    def test_should_check_example14_data(self):
        # given
        s, n = 3, 6
        data = [(0, 2), (1, 2), (2, 2), (3, 2), (4, 2), (5, 2)]
        expected_result = [0, 2, 4, 6, 8, -1]

        # when
        result = network_packets(s, n, data)

        # then
        self.assertEqual(result, expected_result)

    def test_should_check_time_data(self):
        # given
        expected_time = 10

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

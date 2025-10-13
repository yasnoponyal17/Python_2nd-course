import unittest
from sum import find_sum

class TestSum(unittest.TestCase):
    def test_example_1(self):
        nums = [2, 7, 11, 15]
        target = 9
        self.assertEqual(find_sum(nums, target), [0, 1])

    def test_example_2(self):
        nums = [3, 2, 4]
        target = 6
        self.assertEqual(find_sum(nums, target), [1, 2])

    def test_example_3(self):
        nums = [3, 3]
        target = 6
        self.assertEqual(find_sum(nums, target), [0, 1])

    def test_example_4(self):
        nums = [1, 2, 3, 4, 5, 6, 7, 8]
        target = 15
        self.assertEqual(find_sum(nums, target), [6, 7])

    def test_example_5(self):
        nums = [228, 322, 1337, 69, 52, 42, 67]
        target = 389
        self.assertEqual(find_sum(nums, target), [1, 6])
        
unittest.main(verbosity = 2)

import unittest

def find_sum(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)): 
            if nums[i] + nums[j] == target:
                return [i, j]
    return 'Подходящей пары не найдено' 

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
        
unittest.main(verbosity = 2)

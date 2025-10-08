def find_sum(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)): 
            if nums[i] + nums[j] == target:
                return [i, j]
    return 'Подходящей пары не найдено' 


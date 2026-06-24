def twosum(nums, target):
    numMap = {}
    n = len(nums)
    for i in range(n):
        diff = target - nums[i]
        if diff in numMap:
            return [numMap[diff] , i]
        numMap[nums[i]] =i
    return []
print(twosum([2,7,11,15],9))    

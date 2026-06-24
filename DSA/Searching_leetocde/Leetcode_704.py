def search(nums, target):
    n = len(nums)
    for i in range(n):
        if nums[i] == target:
            return i
    return -1   
print(search([-1,0,3,5,9,12],9)) 
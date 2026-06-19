def minSubarraylen(nums,target):
    l = 0
    total = 0
    res = float("inf")
    for r in range(len(nums)):
        total += nums[r]
        while total >= target:
            res = min(r-l+1 , res)
            total -= nums[l]
            l+= 1
    return   0 if res == float("inf") else res
result = minSubarraylen([2,3,1,2,3] , 7)
print(result)
def maxsubarray(nums):
    Maxsub = nums[0]
    currentsum = 0
    for n in nums:
        if currentsum < 0:
            currentsum = 0
        currentsum += n
        Maxsub = max(Maxsub , currentsum)   
    return Maxsub
print(maxsubarray([-2,1,-3,4,-1,2,1,-5,4]))    
#TC is O(n)
# SC is O(1) 
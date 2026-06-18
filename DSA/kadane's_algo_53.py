def maxsubarray(nums):
    Maxsub = nums[0] #Initially consider the 0th index number as maximum sub array
    currentsum = 0   #Initially the current sum is zero
    for n in nums:   
        if currentsum < 0:  # If the current sum becomes less than zero we udate the current sum 
            currentsum = 0   # Reset the current sum to zero we are removing negative numbers 
        currentsum += n   # Adding the next number to the sub array 
        Maxsub = max(Maxsub , currentsum)    
    return Maxsub
print(maxsubarray([-2,1,-3,4,-1,2,1,-5,4]))    
#TC is O(n)
# SC is O(1) 

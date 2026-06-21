def maxSubArray( nums):
    largest_sum = nums[0]
    current_sum = 0
    for n in nums:
      if current_sum  < 0:
         current_sum = 0
      current_sum +=n
      largest_sum = max(current_sum , largest_sum)
    print(largest_sum)   
maxSubArray([-2,1,-3,4,-1,2,1,-5,4])      
def min_value(nums):
 n=len(nums)
 for i in range(n-1):
    min_index=i
    for j in range(i+1,n):
        if nums[j] < nums[min_index]:
           min_index=j
    if min_index != i:
        nums[i],nums[min_index]=nums[min_index],nums[i]
 return nums[0]
nums=[9,8,7,4,1,0,2,3]
print(min_value(nums))
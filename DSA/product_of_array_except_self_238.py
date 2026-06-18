def product(nums):
 n = len(nums)
 result = [1] * len(nums)   # 1[1,2,3,4]1
 prefix = 1                          
 for i in range(n):
    result[i] = prefix 
    prefix *= nums[i]
 postfix = 1
 for i in range(n-1 , -1 , -1):
   result[i] *= postfix
   postfix *= nums[i]
 return result  
print(product([1,2,3,4]))  








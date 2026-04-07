           

# arr = [1,3,9,4,8,1]
# def merge_sort(arr):
#     if len(arr)<=1:
#         return arr
#     mid  = len(arr) // 2
#     left = merge_sort(arr[:mid])
#     right = merge_sort(arr[mid:])
#     return merge(left , right)
# def merge(left, right):
#     result = []
#     i= j = 0
#     while i< len(left) and j<len(right):
#         if left[i] < right[j]:
#             result.append(left[i])
#             i+=1
#         else:
#             result.append(right[j])
#             j+=1
#     result.extend(left[i:])
#     result.extend(right[j:])
#     return result

# print(merge_sort(arr))    

# leetcode 192
# def merge_sort(nums):
#     if len(nums) <=1:
#         return nums
#     mid = len(nums)//2
#     left = merge_sort(nums[:mid])
#     right = merge_sort(nums[mid:])
#     return merge(left , right)
# def merge(left , right):
#     i=j=0
#     merged = []
#     while i<len(left) and j < len(right):
#         if left[i] <= right[j]:
#             merged.append(left[i])
#             i+=1
#         else:
#             merged.append(right[j])
#             j+=1
#             merged += left[i:]
#             merged += right[j:]  
# nums =[5,2,3,1]
# print(merge_sort(nums))                      





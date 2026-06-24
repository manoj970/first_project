def searchInsertposition(nums ,target):
    l = 0
    r = len(nums) -1
    while l<=r:
        mid = (l+r)//2
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            l = mid+1
        r -=1
    return l
print(searchInsertposition([1,3,5,6],5))        

def removeDuplicates(nums):
    if not nums:
        print(0, [])
        return 0
    n = len(nums)
    l = 1
    for r in range(1, n):
        if nums[r] != nums[r-1]:
            nums[l] = nums[r]
            l += 1
    # print the new length and the array up to that length
    print(l, nums[:l])
    return l

if __name__ == '__main__':
    removeDuplicates([0,0,1,1,1,2,2,3,3,4])
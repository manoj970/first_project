def contains_duplicates(nums):
    HashSet = set()
    for n in nums:
        if n in HashSet:
            return True
        HashSet.add(n)
    return False
print(contains_duplicates([1,1,1,3,3,4,3,2,4,2]) )   
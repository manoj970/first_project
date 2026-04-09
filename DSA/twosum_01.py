def twosum(nums , target):
    PrevMap = {} # Hash map to store the index and value in the key : value pair
    for i , n in enumerate(nums):
        diff = target - n
        if diff in PrevMap:   
             return [PrevMap[diff] , i] 
        PrevMap[n] = i
print(twosum([2, 7, 11, 15] , 9))  
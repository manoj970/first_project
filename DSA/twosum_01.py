def twosum(nums , target):
    PrevMap = {} # Hash map to store the index and value in the key : value pair
    for i , n in enumerate(nums):
        diff = target - n # we get the difference the target is 9 and initially num is 2 -- 9-2=7
        if diff in PrevMap:   
             return [PrevMap[diff] , i] 
        PrevMap[n] = i
print(twosum([2, 7, 11, 15] , 9))  
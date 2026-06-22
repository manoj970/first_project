def firstUniquechar(s):
    hashMap = {}
    for ch in s:
        hashMap[ch] =1 + hashMap.get(ch , 0)
    for i , ch in enumerate(s):
        if hashMap[ch] == 1:
            return i
    return -1    
print(firstUniquechar( "leetcode"))    
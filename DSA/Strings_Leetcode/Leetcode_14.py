def longestCommonPrefix(strs):
    word = strs[0]
    n = len(word)
    for i in strs[1:]:
        while word != i[0:n]:
            n-=1
            if n == 0:
                return ""
            word = word[0:n]
    return word 
print(longestCommonPrefix(["flower","flow","flight"]))


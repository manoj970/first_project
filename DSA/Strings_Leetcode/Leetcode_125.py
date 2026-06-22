def ispolindrone(s):
    newStr = ""
    for i in s:
        if i.isalnum():
            newStr += i.lower()
    return newStr == newStr[::-1]
print(ispolindrone( "A man, a plan, a canal: Panama"))
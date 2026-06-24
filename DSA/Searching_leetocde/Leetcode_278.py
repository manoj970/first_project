
bad_version = 4

def isBadVersion(version):
    return version >= bad_version
def badversion(n):
    l = 1
    r = n
    while l <= r:
        mid = (l + r) // 2
        if isBadVersion(mid):
            r = mid - 1
        else:
            l = mid + 1
    return l

print(badversion(5))  
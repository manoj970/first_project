
picked = int(input("Enter the number to be guessed (between 1 and 10): "))

def guess(num):
    if num > picked:
        return -1
    elif num < picked:
        return 1
    else:
        return 0


class Solution(object):
    def guessNumber(self, n):
        l = 1
        r = n

        while l <= r:
            mid = (l + r) // 2
            result = guess(mid)

            if result == 0:
                return mid
            elif result == -1:
                r = mid - 1
            else:
                l = mid + 1


sol = Solution()
print(sol.guessNumber(10))
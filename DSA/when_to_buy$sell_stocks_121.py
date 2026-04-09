def stock(prices):
    left , right = 0 , 1 # left is buy day right is sell day
    MaxProfit = 0     # Initially the profit is 0
    while right < len(prices):
        if prices[left] < prices[right]:
            profit = prices[right] - prices[left]
            MaxProfit = max(MaxProfit , profit) #we use max method and choose the largest profit
        else:
            left = right #if the above condition is false then we shift left to the right position 
        right +=1  # we move the right point until we reach the max profit
    return MaxProfit    
print(stock([7,1,5,3,6,4]))  

# this is two pointer approach
# time complexity is O(n)
#space complexity is O(1)
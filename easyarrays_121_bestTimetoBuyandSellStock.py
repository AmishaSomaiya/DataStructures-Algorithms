"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

leetcode 
easy
arrays 

input : an array prices
output: the maximum profit you can achieve from this transaction. 
If you cannot achieve any profit, return 0

Logic : 2 pointer

approach 1 : left right pointer 
 def maxProfit(prices: List[int]) -> int:
    maxGap = 0
    left, right = 0, 1
    while right < len(prices):
        if prices[left] < prices[right]:
            maxGap = max(maxGap, prices[right] - prices[left])
            right += 1
        else:
            left, right = right, right + 1

    return maxGap
We cannot buy a stock in the future and sell it now in stock market; thus, 
we only need to store the lowest stock price in every iteration. And in next iteration, 
we only need to check whether current stock price is higher than previous lowest stock price. 
If so, then we might need to update maxGap. On the other hand, if current stock price is lower 
than previous lowest price, then we need to update two pointers (left, right).

Time Complexity: O(n), Space Complexity: O(1)

approach 2 : min max
Explanation: Instead of using two variables to store the index of the lowest and current 
price of stock like solution 1, we only need to store the lowest price as iteration goes on. 
If we find current price is less than pervious lowest price, then it is possible that the 
maximum profit might change. Therefore, we might need to update the value of maxGap as shown: 

Time Complexity: O(n), Space Complexity: O(1)

"""

def maxProfit(prices):
    buyprice = float("inf")
    maxgap = 0

    for price in prices :
        buyprice = min(buyprice, price)
        maxgap = max(maxgap, price-buyprice)

    return maxgap


print(maxProfit([7,1,5,3,6,4]))
print(maxProfit([7,6,4,3,1]))
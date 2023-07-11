"""
https://leetcode.com/problems/coin-change/
https://www.youtube.com/watch?v=H9bfqozjoqs

leetcode 322
medium
dynamic programming bottom-up

input : an integer array coins representing coins of different denominations and an integer amount 
representing a total amount of money.
output: the fewest number of coins that you need to make up that amount. If that amount of money 
cannot be made up by any combination of the coins, return -1.

assume that you have an infinite number of each kind of coin.

Logic : 
approach 1 : greedy fr eg : [1,3,4,5], 7
start at the biggest coin, biggest to lowest : 
5+5x 5+4x 5+2x 5+1+1 : 3 coins
but 3+4 = 7 : 2 coins so greedy is not appropriate

approach 2 : backtracking bruteforce
[1,3,4,5] : 4choices then remaining amount = [6.4.3.2]
now 7-(1+6)=0 so when 0 reached, stop
till then continue
now [6,4,3,2]-> consider 2-> can choose 1/3/4/5 -> if we 2-3 = -1 or 2-4=-2
-> negative value -> stop it is not whar we want

bottom-up approach :
dp[0]=0  cannot be made so 0
dp[1]=1  needs only 1 coin to make 1
dp[2]=1  1+dp[1]
dp[3]=1
dp[4]=1
dp[5]=1
dp[6]=2  repeat for all from 0 to 7
dp[7]=1+dp[6]=3 = one possible soln but not minimal
other soln : dp[3]+dp[4]=2  so we in bottomup we will repeat for all coins
i.e for 1,3,4,5
i.e. dp[7] using coin value of 1  -> 1+dp[6]=3
           using coin value of 3 -> dp[3]+dp[4]=2 ->minimal
           using coin value of 4 -> dp[4]+dp[3]=3
           using coin value of 5 -> dp[5]+dp[2]=3 
           then min of all these = 2 = answer

Time Complexity: O(nm)=)(amount*numberofcoins), Space Complexity: O(n), where n is value of 
 and m is the length of coins.

"""

def coinChange(coins, amount):
        # array of size amount+1 since we r going from 0 till amount
        # of value amount+1 = max value
        dp = [amount + 1] * (amount + 1)
        
        # base case 
        dp[0] = 0

        # brute force way from 1 to bottomup
        for a in range(1, amount + 1):
            for c in coins:
                if a - c >= 0:  #nonneg then continue searching
                    # 1 because current coin c
                    # dp[a-c] because say coin 4 and a=7 -> dp[7]=1+dp[7-4] is a possible soln 
                    # recurrence relation
                    dp[a] = min(dp[a], 1 + dp[a - c])
        return dp[amount] if dp[amount] != amount + 1 else -1  #another edge case

print(coinChange([1,2,5], 11))
print(coinChange([2], 3))
print(coinChange([1], 0))
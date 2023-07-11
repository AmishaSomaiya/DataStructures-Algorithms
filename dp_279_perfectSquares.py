"""
https://leetcode.com/problems/perfect-squares/
https://www.youtube.com/watch?v=HLZLwjzIVGo&list=PLot-Xpze53lfOdF3KwpMSFEyfE77zIwiP&index=69

leetcode 279
medium
dynamic programming
same as coin change problem 
here to count min number of squares
bottom up approach 

input : an integer n
output: return the least number of perfect square numbers that sum to n

A perfect square is an integer that is the square of an integer. 
in other words, it is the product of some integer with itself. 
For example, 1, 4, 9, and 16 are perfect squares while 3 and 11 are not.

Logic : 
solve the subprobs before solving the orig prob

Time Complexity: o(n.sqrtn) 

"""

def numSquares(n):
    # dp array to store results of each subprob
    # init dp array to n, can also init to max int
    # but it will be minimum total : n
    # and size is 0 to n : n+1 
    dp = [n]*(n+1)

    # base case : it takes 0 squares to get to the target value 0
    dp[0] = 0

    # iterate thru every target value from 1 to n:
    for target in range(1, n+1):
        # go thru each possible square value
        for s in range(1, target+1):
            square = s*s
            # if we go over : break, stop early
            if target-square < 0:
                break
            # else calc possible soln
            # 1st : no change
            # 2nd : change + 1 sinc we used a square 
            dp[target] = min(dp[target], 1+dp[target - square])
    return dp[n]       



    






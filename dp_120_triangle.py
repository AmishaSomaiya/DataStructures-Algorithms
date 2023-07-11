"""
https://leetcode.com/problems/triangle/

leetcode 120
medium

input : a triangle array
output: return the minimum path sum from top to bottom.

Logic : 
triangle array : nested array
so rewrite this as a tree, but it is not a bst 

recursive dfs:
at every node : to go right or left, then a new subproblem 
till we reach the base case : no children 
so for leaf node, min path sum = itself
then go back up to the parent
min path sum for parent = 
min(parent + min path sum of left child, parent + min path sum of right child)
till u reach root node 

approach 2: dp
dp[leafs] = itself
dp[1 level up parent]=dp[itself]+ min dp of leafs
so for every row, we only need 1 row below it 
i.e. we need to save only 1 row at a time

Time Complexity: o(n^2) since that many eles
space : o(n) i.e. number of rows in input 


"""
from typing import List

def minimumTotal(triangle: List[List[int]]) -> int:
        dp = triangle[-1]  #last row of triangle 

        for row in range(len(triangle) - 2, -1, -1):  #iterate thru every row in input in reverse order 
            # or above as for row in trianle[::-1]
            for col in range(0, row + 1):  #or for i,n in enumerate(row)
                dp[col] = triangle[row][col] + min(dp[col], dp[col + 1])  #itself + min of left and right children, or dp[i] = n+min(dp[i], dp[i+1])

        return dp[0] #root

print(minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]]))
print(minimumTotal([[-10]]))

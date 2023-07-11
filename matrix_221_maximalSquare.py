"""
https://leetcode.com/problems/maximal-square/
https://www.youtube.com/watch?v=6X7Ha2PrDmM&list=PLot-Xpze53lfOdF3KwpMSFEyfE77zIwiP&index=38

leetcode 221
medium
matrix dp bottom up 

input : an m x n binary matrix filled with 0's and 1's,
output: find the largest SQUARE containing only 1's and return its area.

Logic : 
approach1 : brute force : O((mn)^2)
-start from top-left 
-can we atleast make a 1 by 1 to the right, diag and down of the topleft 1x1 
-if yes -> expand the square 
-if no -> then only 1x1 is the max square that can be made at that square 
- check for each cell in entire grid -> o((mn)^2) = very ineff 

approach2 : 
-reduce repeat work by breaking prob into subprobs 
-what is the theoretical biggest SQUARE we can make for a particular ele with regards to the size of dims of the matrix
-so starting at neighbor right, diag, bottom = subprobs 
-move to the next : there will be cells where we already calc earlier = repeated work
-till u go to the base case where there is no more cells left i.e. at the boundary 
-we will go in the reverse order and store max lengths (not areas) : makes it easier

final approach : recursive top down or dp bottom up
Time Complexity: t: O(mn) s: O(mn)

if dp bottom up :
use loop instead of recursion
and use matrix itself instead of cache
saves memory 
"""

from typing import List


def maximalSquare(matrix: List[List[str]]) -> int:
        # recursive 
        ROWS, COLS = len(matrix), len(matrix[0])
        cache = {}  # hashmap each (r, c) position to maxLength of square

        def helper(r, c):
            if r >= ROWS or c >= COLS: #i.e. out of bounds then max length = 0 so return o
                return 0

            # else r,c is inbounds 
            if (r, c) not in cache:  #recursive 
                down = helper(r + 1, c)     #check base case : 1 row down, same col
                right = helper(r, c + 1)    #same row, right col
                diag = helper(r + 1, c + 1) #diag right so incre both 

                cache[(r, c)] = 0  #we want to cahce max area at this position r,c, init=0
                if matrix[r][c] == "1":  #strings, 1st check if r,c position has 1 or 0
                    cache[(r, c)] = 1 + min(down, right, diag)  #if above condition is 1, then len = atleast 1 : 1st term = 1
                    # 2nd term = 1 in above statement if all are 1 else even if 1 of them is 0, min will be 0 o
            return cache[(r, c)]  #if already in cache

        helper(0, 0)  #call helper from top left since going down top-down 
        return max(cache.values()) ** 2

print(maximalSquare([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]))
print(maximalSquare([["0","1"],["1","0"]]))
print(maximalSquare([["0"]]))
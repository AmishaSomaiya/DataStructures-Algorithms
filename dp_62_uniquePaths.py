"""
https://leetcode.com/problems/unique-paths/
https://www.youtube.com/watch?v=IlEsdxuD4lY&list=PLot-Xpze53lfOdF3KwpMSFEyfE77zIwiP&index=41

leetcode 62
medium
dp

input : two integers m and n
output: the number of possible unique paths that the robot can take to reach the bottom-right corner.

Logic : 
-similar to dp416 
-can go only down or to the right
-so from start can go down or right in the entire board
-one block to the right: cannot go in the leftmost col
-one block down : cannot go to the topmost row
-so new start position and where all it can go from there
-also possible to reach stop from each block in the grid
-2 ways to reach every block : after reaching that block, repeat work of down/right after that block 
Time Complexity: O(n * m) s: O(n)
----
from nc :
-mxn grid 
-only 2 choices : right or down, cannot go diag or up 
-goal is to reach end position in bottomright from topleft 

approach :
-recursion with sub problems
-always going to reach destination 
-repeated work : from path 1 : reached cell x, now can go ahead from cell x
-then from another path 2 : also reached cell x, then repeat work for all paths from cell x
-so avoid repeat work with dp by cache result in cache[r][c]
since dfs is expensive 
-so result = right + down : recusrviely 
-base case => choose number of unique paths = 1 for last cell
then go up and/or left to move up to the beginning 
so bottommost row and rightmost col: all 1s 







"""
def uniquePaths(m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        row = [1] * n  #bottom row will be all 1s

        for i in range(m - 1):  #thru all rows except last 1 so m-1 
            newRow = [1] * n  #compute new row above bottom row : inti to all 1s 
            #to avoid edge case to check out of bounds : go thru all cols except right most col since that is always 1 
            # so begin at n-2 till the beginning in reverse order 
            for j in range(n - 2, -1, -1):  
                newRow[j] = newRow[j + 1] + row[j]  #current new value = value below(i.e old row row[j]) + col to right(i.e newRow[j+1])
            row = newRow  #update old row as newrow, till we reach top row 
        return row[0]  #return 1st value in top row 

        # O(n * m) O(n)

print(uniquePaths(3,7))
print(uniquePaths(3,2))
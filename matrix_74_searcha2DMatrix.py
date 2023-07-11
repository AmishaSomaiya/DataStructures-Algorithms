"""
https://leetcode.com/problems/search-a-2d-matrix/
https://www.youtube.com/watch?v=Ber2pi2C0j0&list=PLot-Xpze53lfOdF3KwpMSFEyfE77zIwiP&index=66

leetcode 74
medium
matrix
double binary search 

input : given an m x n integer matrix matrix with the following two properties:
Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
and Given an integer target
output: return true if target is in matrix or false otherwise.

Logic : 
-as per given 2 conditions -> the enitre matrix is sorted

approach 1 : brute force : o(m.n)
go thru entire matrix to search ele by ele 

approach 2 : using 1st property 
-use the property that matrix is sorted
-suppose assume only sorted array available and not matrix 
since sorted array given : then can use binary search 
-so for an array of size n : time comp = o(logn) for binary search on 1 array 
-now m rows : m arrays given : then o(mlogn)

approach 3 : 
now using 2nd property :
#1. first use bin search just to figure out which row to search :o(logm)
#2. once we got the row, do second binary search on that row only : logn 
= o(logm+logn) = o(log(m*n))

Time Complexity: O(log(m * n))

"""
from typing import List


def searchMatrix(matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])  #dims of the matrix 

        #1st binary search 
        top, bot = 0, ROWS - 1  #2 pointers to find the row 
        while top <= bot:  #till u find the target row or till the end i.e. target row doesnt even exist in the matrix 
            row = (top + bot) // 2  #middle row for bin search
            # case 1 : target value is larger than largest value in this row
            #then we need to check rows with even larger values 
            # so top = mid + 1 
            if target > matrix[row][-1]:
                top = row + 1  
            # else case 
            elif target < matrix[row][0]:
                bot = row - 1
            # else it is current row itself so break 
            else:
                break

        # if none of the rows have the target value, return immed
        if not (top <= bot):
            return False
        
        # else run second portion of binary search 
        row = (top + bot) // 2
        l, r = 0, COLS - 1  #pointers for left and right 
        while l <= r:
            m = (l + r) // 2
            if target > matrix[row][m]: #search towards right 
                l = m + 1
            elif target < matrix[row][m]: #search towards left 
                r = m - 1
            else:  #target found
                return True
        #target not found 
        return False

print(searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3))
print(searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13))



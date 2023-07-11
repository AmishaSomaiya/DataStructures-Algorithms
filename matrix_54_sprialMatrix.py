"""
https://leetcode.com/problems/spiral-matrix/
https://www.youtube.com/watch?v=BJnMZNwUk1M&list=PLot-Xpze53lfOdF3KwpMSFEyfE77zIwiP&index=32

leetcode 54
medium
matrix 

input : m x n matrix
output: return all elements of the matrix in spiral order

Logic : 
-cross out eles as u move, 
all right -> then all down -> then all left -> all up (uncrossed) 
-> update left right top and bottom boundaries 
-> repeat till boundaries overlap(intersect) -> stop 

1. 4 pointers : 
- left and top initialize at top left 
- right initialize 1 after the topright
- bottom initialize 1 below the bottomleft 

2. output = list/array

3. starting point = top left point 


Time Complexity: O(mn) i.e. dims of matrix, space : O(1) if we do not count result var as extra memory 


"""

from typing import List


def spiralOrder(matrix: List[List[int]]) -> List[int]:
        res = []  
        left, right = 0, len(matrix[0])  #4 pointers 
        top, bottom = 0, len(matrix)

        while left < right and top < bottom:  #till no pointers intersect 
            # get every i in the top row
            for i in range(left, right):
                res.append(matrix[top][i])  #simply append the element
            # once the top row is completed, update the top row by decre by 1 
            top += 1 #shift right 

            # get every i in the right col
            for i in range(top, bottom):  #top already updated so nothing else to do for top
                res.append(matrix[i][right - 1])
            # update right pointer : shift left 
            right -= 1 
            if not (left < right and top < bottom):  #pointers intersect, break out of loop 
                break
            # get every i in the bottom row
            for i in range(right - 1, left - 1, -1):
                res.append(matrix[bottom - 1][i])

            # update bottom pointer : shift up 
            bottom -= 1
            # get every i in the left col
            for i in range(bottom - 1, top - 1, -1):
                res.append(matrix[i][left])
            # update left : shift to right 
            left += 1

        return res

print(spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))
print(spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))


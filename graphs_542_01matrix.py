"""
https://leetcode.com/problems/01-matrix/

leetcode 542
medium
graphs, dynamic programming

input : m x n binary matrix mat
output: the distance of the nearest 0 for each cell (list of list of int)

Logic : dynamic programming

Explanation: 
Observe that for each 1-cell (the value of cell is one), its minimum distance 
to 0-cell (the value of cell is zero) must come from its four neighbors. We can perform a 
two-pass algorithm to solve this problem. Iterate the matrix from top->bottom & left->right 
and bottom->top & right->left. The direction does not matter since if we iterate the matrix 
from top->bottom & left->right, we are simply finding the shortest among all paths to the 
top/left/top-left of a given node. As long as you search in all directions, the answer will 
be correct.

pseudo code :
-declare array of distances to be returned
-2 pass algorithm to calc distances : 
-loop over matrix : top->bottm, left->right
-second pass      : bottom->top, right->left

Time Complexity: O(m*n), Space Complexity: O(1), 
where m is the number of row and n is the number of column.

"""
def updateMatrix(mat):
    distance = [[float("inf") for _ in range(len(mat[0]))] for _ in range(len(mat))]

    for row in range(len(mat)):
        for column in range(len(mat[0])):
            if mat[row][column]==0:
                distance[row][column]=0
            else :
                if row > 0:
                    distance[row][column] = min(distance[row][column], distance[row-1][column] + 1)
                if column > 0:
                    distance[row][column] = min(distance[row][column], distance[row][column-1] + 1)

    for row in range(len(mat)-1, -1, -1):
        for column in range(len(mat[0])-1,-1,-1):
            if row < len(mat)-1:
                distance[row][column] = min(distance[row][column], distance[row+1][column] + 1)
            if column < len(mat[0])-1:
                distance[row][column] = min(distance[row][column], distance[row][column+1] + 1)

    return distance 


print(updateMatrix([[0,0,0],[0,1,0],[0,0,0]]))
print(updateMatrix([[0,0,0],[0,1,0],[1,1,1]]))
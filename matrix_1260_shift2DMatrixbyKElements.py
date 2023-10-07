"""
https://leetcode.com/problems/shift-2d-grid/  

leetcode 1260
easy
matrix

input :  a 2D grid of size m x n and an integer k
output: You need to shift the grid k times.

In one shift operation:

Element at grid[i][j] moves to grid[i][j + 1].
Element at grid[i][n - 1] moves to grid[i + 1][0].
Element at grid[m - 1][n - 1] moves to grid[0][0].
Return the 2D grid after applying shift operation k times.

Logic : convert 2d matrix to array, shift and convert array back to 2d matrix 

Time Complexity: o(nm)
Space : o(nm)

"""

class Solution:
    def shiftGrid(self, grid, k: int):
        m,n = len(grid), len(grid[0])

        def matrix2array(r,c):
            index = r*n + c
            return index
        
        def array2matrix(index):
            row = index//n
            col = index%n
            return (row,col)
        
        res = [[0]*n for i in range(m)]

        for r in range(m):
            for c in range(n):
                index = matrix2array(r,c)
                shiftedindex = (index+k)%(m*n)
                row, col = array2matrix(shiftedindex)
                res[row][col] = grid[r][c]

        return res 
    

        
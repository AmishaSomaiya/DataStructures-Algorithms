"""
https://leetcode.com/problems/set-matrix-zeroes/
https://www.youtube.com/watch?v=T41rL0L3Pnw&list=PLot-Xpze53lfOdF3KwpMSFEyfE77zIwiP&index=22

leetcode 73
medium
matrix 

input : an m x n integer matrix matrix
output: if an element is 0, set its entire row and column to 0's.
INPLACE 

Logic : 
Follow up:
A straightforward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?

approach 1 : O(mn) memory : not efficient 
-declare a copy of the matrix, so changes made to copy, and read values from orig matrix 
-go thru every position, whenever 0 encountered:
-make that row and col all 0s 
-but repeated work so not efficient

approach 2 : O(m+n) memory soln, time : O(m.n)
-there is a fixed amount of rows and cols 
-worst case -> every row and col to be set to 0
-so we need lesser memory than entire copy
-we need 1 array for #cols and 1 array for #rows
and mark these : whether that row/col has to be filled with 0s or not
-then in the end do all filling together in place
-so copy not needed

approach 3 : O(1) memory soln
-so now instead of considering separate memory for row and col arrays 
-consider these arrays to be part of matrix itself as first row and first col
-and col 1 ele < row to avoid overlap + 1 extra cell 
-so o(1) memory because of 1 single extra cell 
-this works because top-bottom left-right so nothing interferes with anything 

"""

def setZeroes(matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        # O(1)
        ROWS, COLS = len(matrix), len(matrix[0])  #number of rows and cols
        rowZero = False #1 extra var only 

        # determine which rows/cols need to be zero, iterate thru all rows and cols
        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0  #if a 0 is encountered, make corresponding ele in 0th row and col 0 i.e. 
                    # matrix[0][c] and matrix[r][0] make these to 0
                    if r > 0: #but not for this position to avoid overlap as discussed earlier
                        matrix[r][0] = 0
                    else:  #this var 
                        rowZero = True

        # 1 more time, loop thru each row and col position :
        # to actually make the values 0 
        for r in range(1, ROWS):  #skip 1st row and 1st col to be handled separately later 
            for c in range(1, COLS):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0 #make current position as 0

        if matrix[0][0] == 0:
            for r in range(ROWS):
                matrix[r][0] = 0 #zeroing the first col of the matrix 

        if rowZero:
            for c in range(COLS):
                matrix[0][c] = 0 #zeroing the first row of the matrix 

        print(matrix)

setZeroes([[1,1,1],[1,0,1],[1,1,1]])
setZeroes([[0,1,2,0],[3,4,5,2],[1,3,1,5]])
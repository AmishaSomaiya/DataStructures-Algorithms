"""
https://leetcode.com/problems/rotate-image/
https://www.youtube.com/watch?v=fMSJSS7eO1w&list=PLot-Xpze53lfOdF3KwpMSFEyfE77zIwiP&index=15

leetcode 48
medium
matrix

input : n x n 2D matrix representing an image
output: rotate the image by 90 degrees (clockwise) in-place 

Logic : 
first the outer boundary then the inner square 


Time Complexity: O(n^2), s: O(1)

"""
def rotate(matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        l, r = 0, len(matrix) - 1  #left and right boundaries
        while l < r:  #till l<r
            for i in range(r - l): #iterate thru entire row except last element 
                top, bottom = l, r #top and bottom pointers = l,r because square mat 

                # save the topleft
                topLeft = matrix[top][l + i]  #save this 1 variable 

                # now all movements in reverse order 
                # i.e. rotation is clockwise so we will do anticlockwise movements 
                # move bottom left into top left
                matrix[top][l + i] = matrix[bottom - i][l]

                # move bottom right into bottom left
                matrix[bottom - i][l] = matrix[bottom][r - i]

                # move top right into bottom right
                matrix[bottom][r - i] = matrix[top + i][r]

                # move top left into top right
                matrix[top + i][r] = topLeft

            # layered rotation : outer layer above 
            # rotation of matrix is such that topleft -> 1 position to the right 
            #                                 topright -> 1 position down
            #                               bottomright-> 1 position to left
            #                               bottomleft -> 1 position up  
            # i variable accordingly in the above element shifts  
            
            #update pointers for submatrix or inner layer rotation 
            r -= 1   
            l += 1
        print(matrix)


rotate([[1,2,3],[4,5,6],[7,8,9]])
rotate([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]])
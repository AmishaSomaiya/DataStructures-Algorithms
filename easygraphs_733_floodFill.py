"""
https://leetcode.com/problems/combination-sum/

leetcode 733
easy
graphs

Logic : DFS

input : m x n integer grid image, three integers sr, sc, and color
output: list of list of int : the modified image after performing the flood fill.

explanation : perform DFS, check boundary conditions when searched in all 4 directions

Time Complexity: O(m * n), Space Complexity: O(m * n) for recursion stack, where m is the 
number of row and n is the number of column.

"""

def floodFill(image, sr, sc, color):
    def search_and_fill(row: int, column: int) -> None:
        if image[row][column] == previos_color:
            image[row][column] = color
            if row + 1 < number_of_rows:
                search_and_fill(row+1, column)
            if row >= 1:
                search_and_fill(row-1, column)
            if column + 1 < number_of_columns:
                search_and_fill(row, column+1)
            if column >= 1:
                search_and_fill(row, column-1)

    number_of_columns, number_of_rows = len(image[0]), len(image)
    previos_color = image[sr][sc]
    if previos_color == color:
        return image

    search_and_fill(sr, sc)
    return image


print(floodFill([[1,1,1],[1,1,0],[1,0,1]],1,1,2))
print(floodFill([[0,0,0],[0,0,0]],0,0,0))
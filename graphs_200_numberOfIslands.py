"""
https://leetcode.com/problems/number-of-islands/

leetcode 200
medium
graphs 

input : grid = matrix = list of lists of str
output: number of islands

logic : DFS
Everytime we find a land ("1"), we perform DFS (depth-first search) to 
find all of the land in this island and change it to water ("0") so that we will not count 
it again in further iterations. After DFS, we have fully explored this particular island. 
Notice that it is feasible to change it to another character whatever you like except "1".


pseudocode :
if boundaries exceeded -> return 
if ele = 0 -> return
else (i.e. when a 1 is found):
    1. change it to 0
    2. perform dfs on all its neighbors i.e. 
       (row-1,col), (row+1,col), (row,col-1), (row,col+1)
    3. initially number of islands = 0
    4. loop on matrix : nested loop on rows and cols :
        if ele = 1:
            perform dfs on this ele
            incre number of islands
    5. return the number of elements

Time Complexity: O(n * m), Space Complexity: O(n * m), 
where n is the number of row and m is the number of column.

"""

from typing import List

def numIslands(grid: List[List[str]]) -> int:
    def dfs(row: int, column: int) -> None:

        exceed_boundaries = row<0 or column<0 or row>=numberofrows or column>=numberofcol
        if exceed_boundaries or grid[row][column]=="0":
            return
        
        grid[row][column]="0"
        dfs(row-1,column)
        dfs(row+1,column)
        dfs(row,column-1)
        dfs(row,column+1)   #dfs function ends

    numberofislands = 0
    numberofrows = len(grid)
    numberofcol = len(grid[0])

    for i in range(numberofrows):
        for j in range(numberofcol):
            if grid[i][j] == "1":
                dfs(i,j)
                numberofislands +=1

    return numberofislands
    

grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]

print(numIslands(grid))


grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]

print(numIslands(grid))
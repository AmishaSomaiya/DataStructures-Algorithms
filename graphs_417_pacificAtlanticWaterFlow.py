"""
https://leetcode.com/problems/pacific-atlantic-water-flow/
https://www.youtube.com/watch?v=s-VkcjHqkGI&list=PLot-Xpze53lfOdF3KwpMSFEyfE77zIwiP&index=47

leetcode 417
medium
graph 

input : 
output: 

Logic : 
if a cell can reach both oceans, then we add that cell to the result 
i.e. has value >= adjacent cell then water can flow from it to adjacent cell till border 
-cannot go diag (usual in graph probs)

approach 1 : brute force :
start from every cell and perform dfs/bfs and check if it can reach top/left border and right/bottom border
if it can reach then add to soln, else dont add it
time complexity : depends on size of grid : O((m.n)^2)

approach 2 : 
cut out on repeated work and avoid starting out from each cell : doesnt work 

next approach : O(mn)
everything in the top row or left column: borders the pacific ocean :
so can reach the pacific ocean
similarly for atlantic ocean : everything in bottom row or right col can reach the atlantic ocean
in the end, go thru entire grid and find which positions can reach both oceans
add these to result
-visiting each cell in the grid only once so o(mn)

maintain hashset of visited nodes 
Time Complexity: O(mn)

"""

from typing import List


def pacificAtlantic(heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])  #dims of grid 
        pac, atl = set(), set()  #2 hashsets 

        def dfs(r, c, visit, prevHeight): #called down 
            if (
                (r, c) in visit  #if this position visited
                or r < 0     #or out of bounds 
                or c < 0
                or r == ROWS
                or c == COLS
                or heights[r][c] < prevHeight #or condition not satisfied 
            ):
                return #then return 
            # else : if condition met : then add this position to visit 
            visit.add((r, c))
            # perform dfs on all 4 neighbors 
            dfs(r + 1, c, visit, heights[r][c])
            dfs(r - 1, c, visit, heights[r][c])
            dfs(r, c + 1, visit, heights[r][c])
            dfs(r, c - 1, visit, heights[r][c])

        # for 1st row and last row 
        for c in range(COLS): 
            #every single position in 1st row  
            dfs(0, c, pac, heights[0][c])  #parameters : row, col, i.e position, visitset, height to compare
            #every single position in last row  
            dfs(ROWS - 1, c, atl, heights[ROWS - 1][c]) #parameters : row, col, visitset, height to compare

        # for 1st col(pc) and last col(atlantic ocean)
        for r in range(ROWS):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, COLS - 1, atl, heights[r][COLS - 1])

        # after above 2, go thru every single position in the grid, 
        res = []  #list 
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pac and (r, c) in atl:  #check if this position is in both
                    res.append([r, c]) #append position as sublist to result list 
        return res

print(pacificAtlantic([[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]))
print(pacificAtlantic([[1]]))
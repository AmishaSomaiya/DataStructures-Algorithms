"""
https://leetcode.com/problems/rotting-oranges/
https://www.youtube.com/watch?v=y704fEOx0s0
https://neetcode.io/practice


leetcode 994
medium
graphs, multi-source BFS

input : m x n grid
output: the minimum number of minutes that must elapse until no cell has a 
fresh orange. If this is impossible, return -1.

Logic : 
-if there is no rotten orange in any cell, it is not possible to rot all oranges, 
so return -1
-if only 1 rotten orange to begin with -> easy case
-if multiple oranges rotten to begin with ->
 -> DFS will not work here as optimum
 -> BFS helpful here since we do not need to finish DFS on one and then begin other
 instead can begin simult at multiple sources    

pseudo-code : 
- keep count of how many fresh oranges are there initially : preproc
- initialize queue (deque) with the rotten oranges (1 or more) at the beginning 
- pop out every initial rotten orange = 1 unit of time
- add next rotten oranges (neighbors of initial rotten oranges)
- remove initial rotten oranges from queue
- when the recently added rotten oranges popped = second unit of time
- repeat till all oranges done i.e. queue is empty
- possible that some orange might reamin fresh (if disconnected from other oranges)
- so when queue is empty if number of fresh oranges !=0 -> some oranges disconn has 
remained fresh -> return -1
else return units of time needed to rot all oranges


Time Complexity: O(m * n), Space Complexity: O(m+n), 
where m is the number of row and n is the number of column.

"""
from collections import deque
def orangesRotting(grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        q = deque()  #initialize queue
        fresh = 0    #to keep track of fresh oranges
        time = 0     #time to return

        #pre-processing to find number of fresh oranges 
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r, c))

        # directions where we will search
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        # while there are fresh oranges still and queue is not empty
        while fresh > 0 and q:
            length = len(q)
            for i in range(length):
                r, c = q.popleft()

                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    # if in bounds and nonrotten, make rotten
                    # and add to q
                    if (
                        row in range(len(grid))
                        and col in range(len(grid[0]))
                        and grid[row][col] == 1
                    ):
                        grid[row][col] = 2
                        q.append((row, col))
                        fresh -= 1
            time += 1
        return time if fresh == 0 else -1


print(orangesRotting([[2,1,1],[1,1,0],[0,1,1]]))
print(orangesRotting([[2,1,1],[0,1,1],[1,0,1]]))
print(orangesRotting([[0,2]]))
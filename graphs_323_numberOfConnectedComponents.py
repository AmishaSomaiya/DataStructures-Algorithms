"""
premium leetcode 323
leetcode 547 

https://www.youtube.com/watch?v=8f1XPm4WOUc&list=PLot-Xpze53lfOdF3KwpMSFEyfE77zIwiP&index=41
@12:03 code different  

medium
graphs 

input : integer n and array edges
output: the number of conn components in graph 

Logic : 
-not too many edge cases 
-if n nodes : not connected : then return n 
-if n=0 return 0

approach1 : O(e+v) since we need to go thru every single edge 
to build the adjacency list and every single node while performing dfs traversal 
-edges given as list of edges
-convert it to adjacency list 
-do dfs on entire graph : go thru each node starting from 0
-do dfs from 0 : mark nodes as visited as and when we visit them 
-so 1 dfs search gave us 1 conn comp
-then begin dfs on next node :but if it is visited, we do not add it 
as new conn comp

approach2 : union find 
-maintain 2 arrays : parent array : nodes where ele = node number = index number initially 
-i.e. each node is parent for itself initially
-so init n trees : 1 for each node so #conn comp init = n
-now as we go thru each edge, we merge conn comp, so as we merge, decre conn comp by 1 
= union find 
-also optimization : maintain rank of each conn comp = size of each conn comp 
-init rank for each = 1
-consider edge list : [[0,1],[1,2],[3,4]]
-so when 0 merged with 1 : rank of 0 will be incre = size of the parent
but rank of 1 unchanged 
-so we can merge smaller conn comp underneath bigger rather than vice-versa 
-next edge = [1,2] but 1 is not a parent so :
    1. even though [1,2], we will connect 0,2 since parent is 0 so to min height of tree, rank of 0 incre to 3 
    2. we will connect 2 to 0,1 and not vice-versa to connect smaller to larger 
-parent array maintained will help find which node is the parent : for connecting 
-init number of conn comp = 5, did union operation 3 different times : so finally left with 2 conn comp 
Time Complexity:

"""

from typing import List


class UnionFind:
    def __init__(self):
        self.f = {}

    def findParent(self, x):
        y = self.f.get(x, x)
        if x != y:
            y = self.f[x] = self.findParent(y)
        return y

    def union(self, x, y):
        self.f[self.findParent(x)] = self.findParent(y)



def countComponents(n: int, edges: List[List[int]]) -> int:
        dsu = UnionFind()
        for a, b in edges:
            dsu.union(a, b)
        return len(set(dsu.findParent(x) for x in range(n)))



print(countComponents(5, [[0,1],[1,2],[3,4]]))

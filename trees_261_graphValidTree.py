"""
https://leetcode.com/problems/combination-sum/

leetcode 261 premium
medium

input : n nodes, list of undirected edges(go both ways)
output: write a func to check if these edges make up a valid tree

Logic : 
1. trees do not have cycles 
2. trees are connected 


eg:
         0
    1`  2    3
   4

approach:
-create adjacency list 
-traverse(dfs) starting from any node and check 
-empty graph is a tree : return true
-if #visited nodes = #nodes -> connected 
-if starting node visited again and still some nodes yet to be visited -> cycle
 so return false immediately
-maintain hashset for tracking visited nodes
-start from root -> add to hashset
-go to most adjacent neighbor -> add to hashset
-from here visit the unvisited neighbors so we dont go back to the root unnecessarily
because root is also 1 of the neighbors of 1 
to avoid the false positive 
use additional value : previous
so from 1 go only down and not back to root(prev)
add new node to visit set
now all neighbors of 1 are done 
so base case : return true for this case
go aheaf to 2 and so on 
-prev for root : -1 
1st condn : no loop detected so no cycles
2nd condn : #nodes in visit set = #nodes so connected 



Time Complexity: o(e+v)

"""
# Problem is free on Lintcode
from typing import List


class Solution:
    """
    @param n: An integer
    @param edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """

    def validTree(self, n, edges):
        # base case 1: no nodes given: empty graph :  return true 
        if not n:
            return True
        
        # create adjacency list : hashmap , empty list init
        adj = {i: [] for i in range(n)}
        # undirected so both ways 
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        visit = set()  #hashset to track visited nodes 

        # i: node we r visiting, prev: node to avoid false positives 
        # dfs func inside outer func so vars like adj need not be passed to dfs separately
        def dfs(i, prev):
            # base case 2:
            # if revisiting an already visited node, return false immmediately
            if i in visit:
                return False

            # else
            # i has not been visited yet : 
            visit.add(i)
            for j in adj[i]:
                if j == prev:  #skip 
                    continue
                if not dfs(j, i):  #perform dfs on neighbor of i but not yet visited 
                    return False #if not means loop detected
            return True  #else no loop 

        # now call dfs starting at node 0 with prev=-1 
        return dfs(0, -1) and n == len(visit)  #2 conditions : no cycle and connected as discussed above 
    
    
    
    # alternative solution via DSU O(ElogV) time complexity and 
    # save some space as we don't recreate graph\tree into adjacency list prior dfs and loop over the edge list directly
    
    
    # @param n: An integer
    # @param edges: a list of undirected edges
    # @return: true if it's a valid tree, or false
    
    def __find(self, n: int) -> int:
        while n != self.parents.get(n, n):
            n = self.parents.get(n, n)
        return n

    def __connect(self, n: int, m: int) -> None:
        pn = self.__find(n)
        pm = self.__find(m)
        if pn == pm:
            return
        if self.heights.get(pn, 1) > self.heights.get(pm, 1):
            self.parents[pn] = pm
        else:
            self.parents[pm] = pn
            self.heights[pm] = self.heights.get(pn, 1) + 1
        self.components -= 1

    def valid_tree(self, n: int, edges: List[List[int]]) -> bool:
        # init here as not sure that ctor will be re-invoked in different tests
        self.parents = {}
        self.heights = {}
        self.components = n

        for e1, e2 in edges:
            if self.__find(e1) == self.__find(e2):  # 'redundant' edge
                return False
            self.__connect(e1, e2)

        return self.components == 1  # forest contains one tree






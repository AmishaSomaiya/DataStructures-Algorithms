"""
https://leetcode.com/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero/
https://www.youtube.com/watch?v=m17yOR5_PpI&list=PLot-Xpze53lfOdF3KwpMSFEyfE77zIwiP&index=52

leetcode 1466
medium
BFS 

input : 
output: 

Logic :
-no loops
-connected since n-1 edges

-to connect everything to 0, look at neighbors of 0: can neighbors reach 0
-then check backwards : if neighbors of neighors can reach those neighbors 
and so on  

Time Complexity: visit every node only once : O(n), space : O(n)

"""

from typing import List


def minReorder(n: int, connections: List[List[int]]) -> int:
# start at city 0
# recursively check its neighbors
# count outgoing edges

    # take each connection and add to hash set 
    edges = {(a,b) for a,b in connections} #set comprehension

    # know each nodes neighbors (not whether we can reach neighbors or not, just neighbors )
    # using hashmap
    # dict comprehension
    # each city will have empty list initially 
    neighbors = {city:[] for city in range(n)}

    # hashset to keep track of visited nodes so we visit each node only once
    visit = set()

    # to count number of edges we need to change : int variable
    changes = 0

    # fill neighbors hashmap
    for a, b in connections:
        neighbors[a].append(b)   #neighbors of a include b and neighbors of b include a
        neighbors[b].append(a)

    # function to traverse graph 
    # dfs recursively 
    def dfs(city):
        # nonlocal so that no need to pass in every func call
        nonlocal edges, neighbors, visit, changes
        # for each city, iterate thru its neighbors 
        for neighbor in neighbors[city]:
            # if neighbor already visited, do not traverse again
            if neighbor in visit:
                continue
            # check if this neighbor can reach city 0
            if (neighbor, city) not in edges :
                changes += 1
            visit.add(neighbor)
            # recursively run dfs to check if all neighbors can also reach city 0: i.e. propagate changes 
            dfs(neighbor)
    visit.add(0)
    # func call from starting point 
    dfs(0)
    return changes 


print(minReorder(6,[[0,1],[1,3],[2,3],[4,0],[4,5]]))
print(minReorder(5,[[1,0],[1,2],[3,2],[3,4]]))
print(minReorder(3,[[1,0],[2,0]]))





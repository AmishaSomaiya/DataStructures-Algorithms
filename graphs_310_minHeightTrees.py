"""
https://leetcode.com/problems/minimum-height-trees/
https://www.youtube.com/watch?v=ivl6BHJVcB0
https://github.com/yuchia0221/Grind-75/tree/main/Graph/310-MinimumHeightTrees

leetcode 310
medium
graphs

logic: topological sorting 

explanation:
input : a tree of n nodes labelled from 0 to n - 1, and an array of n - 1 edges 
where edges[i] = [ai, bi] 
output: list of all MHTs root labels

consider A->B->C->D->E->F
A and E are leaf nodes so trees from A or F will not be MHT. 
So consider the remaining nodes : B,C,D,F., again B and F are leaf
so tree rooted at the middle node (if odd number of nodes) or the middle 2 nodes if 
even number of nodes : these trees will be MHTs.

another way to look at this : look at the longest path. leaf nodes do not contribute
to the MHT root. i.e. nodes with degree 1 do not contribute to the MHT root.

so in the code, remove the 1 degree nodes and decrement the degree of other nodes. repeat till
atmost 2 nodes of degree 1 each remain. so answer will be these nodes. = topological sorting

pseudo-code : 
-create a list to return the output
-if number of nodes <=0, return empty list
-if number of nodes = 1, only 1 node and no edges, simply add 0 to the list and return it

Time Complexity: O(N), Space Complexity: O(N), where N is the number of nodes.

"""

def findMinHeightTrees(n, edges):
    # Edge Cases: only one node in the graph
    if not edges:
        return [0]
    
    # Build up adjacency list
    adjacencylist = [set() for _ in range(n)]
    for start, end in edges:
        adjacencylist[start].add(end)
        adjacencylist[end].add(start)

     # Find the leaf nodes of the tree
    leaves = []
    for index, neighbors in enumerate(adjacencylist):
        if (len(neighbors) == 1):
            leaves.append(index)
    
    # Remove leaf nodes until there is less than or equal to 2 nodes
    remainingleaf = n
    while remainingleaf > 2:
        newleaves = []
        remainingleaf -= len(leaves)
        for _ in range(len(leaves)):
            leafnode = leaves.pop()
            neighbor = adjacencylist[leafnode].pop()
            adjacencylist[neighbor].remove(leafnode)
            if len(adjacencylist[neighbor]) == 1:
                newleaves.append(neighbor)
        leaves = newleaves

    return leaves


print(findMinHeightTrees(4, [[1,0],[1,2],[1,3]]))
print(findMinHeightTrees(6, [[3,0],[3,1],[3,2],[3,4],[5,4]]))
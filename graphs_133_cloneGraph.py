"""
https://leetcode.com/problems/clone-graph/
https://www.youtube.com/watch?v=mQeF6bN8hMk&list=PLot-Xpze53lfOdF3KwpMSFEyfE77zIwiP&index=30

leetcode 133
medium
bfs + hashtable 

input : node class : value of node (int), list of neighbors
output: graph clone

logic : BFS + Hashtable 
Simply perform breadth-first search (BFS) to solve this problem 
and use a hash table to track vistied and cloned nodes.

pseudocode :
if node is empty(none) then return node
else: 
    declare a queue of 1 element i.e. node
    create a hashtable with key=node value, value=node
    loop on queue :
        popleft 1 element
        extract value for this ele from hashtable
        loop on neighbors list of this value:
            if neighbor not in hashtable :
                add this neighbor to hashtable and to queue
return value of node from hashtable 

Time Complexity: O(V + E), Space Complexity: O(V), 
where V is the total number of nodes and E is the total number of edges.

"""
# # Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

def cloneGraph(node: "Node") -> "Node":
        oldToNew = {}   #hashmap mapping old nodes to new nodes 

        def dfs(node):  
            if node in oldToNew:  #if already in hashmap, no need to make new clone 
                return oldToNew[node]  #only return the clone 

            # else create that clone called copy with val = value of original node 
            copy = Node(node.val)
            # add copy to hashmap 
            oldToNew[node] = copy
            # make copies of every single neighbor of original node and run dfs on each neighbor 
            # it returns copy = new node 
            # append dfs call to the list of neighbors of new node = copy 
            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))
            return copy  #then return copy just made to the current function call 

        return dfs(node) if node else None  #call dfs with original node given, return None if given node is null 

# from collections import deque
# def cloneGraph(node):
#     if node is None:
#         return node

#     queue = deque([node])
#     clones = {node.val: Node(node.val)}
#     while queue:
#         current = queue.popleft()
#         current_clone = clones[current.val]
#         for neighbor in current.neighbors:
#             if neighbor.val not in clones:
#                 clones[neighbor.val] = Node(neighbor.val)
#                 queue.append(neighbor)

#             current_clone.neighbors.append(clones[neighbor.val])

#     return clones[node.val]

print(cloneGraph([[2,4],[1,3],[2,4],[1,3]]))
print(cloneGraph([[]]))
print(cloneGraph([]))
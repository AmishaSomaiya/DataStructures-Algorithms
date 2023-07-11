"""
https://leetcode.com/problems/binary-tree-level-order-traversal/
https://www.youtube.com/watch?v=6ZnyEApgFYg&list=PLot-Xpze53lfOdF3KwpMSFEyfE77zIwiP&index=56

leetcode 102
medium
trees, bfs 

input : binary tree
output: level order traversal of its nodes 
i.e. list of lists : root to leaf sublists at each level 

Logic : 
1. hwo to make lists level wise : bfs
2. implement bfs using queue : fifo 

-start from root : added to queue : pop it add to result
-go to children of root : add to queue : pop from left to right, add its children to queue
-go to next level 
-end when no other level or nodes left in queue 


Time Complexity: linear : o(n) : visiting every single node only once 
space : o(n) because queue ds used and it can have max of o(n/2) 
because biggest level in bst can have max of n/2 nodes ~ O(n)


"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque
from typing import Optional, List


def levelOrder(root: Optional[TreeNode]) -> List[List[int]]:
        res = []  #init res arr to return 
        q = deque()  #queue
        if root:  #start by appending root to queue
            q.append(root)

        while q:  #while queue is not empty : ie no nodes left in any level 
            val = [] #list for 1 level 

            for i in range(len(q)):  #iterate thru 1 level at a time 
                node = q.popleft() #pop from left : fifo 
                if node : #node can be empty so check if node is not empty 
                    val.append(node.val) #append node to result 
                    if node.left:  #add children to queue
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
            #after 1 level is done 
            # if level is not empty: 
            if val: 
                res.append(val)  #append this sublist to result to return 
        return res  #return result 
    
print(levelOrder([3,9,20,None,None,15,7]))
print(levelOrder([1]))
print(levelOrder([]))


"""
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/   
https://www.youtube.com/watch?v=gs2LMfuOR9k&list=PLot-Xpze53lfQmTEztbgdp8ALEoydvnRQ&index=18

leetcode 235
easy

input : a binary search tree (BST) root and 2 nodes 
output: find the lowest common ancestor (LCA) node of two given nodes in the BST.

Logic : 
-LCA of p and q means either p and q are descendents of this LCA node or it itself is p or q
and other node is descendent of it
-begin from root, because it is common ancestor for all nodes, not necesssarily LCA but CA
-eg. 1: 2<(root=6) so goes into left subtree
8>root so goes into right subtree
so in this specific eg., since p=2 is in left subtree and q=8 is in right subtree, there is no common 
node other than the root.   

Time Complexity: 

"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        cur = root
        while cur:
            if p.val > cur.val and q.val > cur.val:
                cur = cur.right
            elif p.val < cur.val and q.val < cur.val:
                cur = cur.left
            else:
                return cur
            
'''
testing :
Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6
Explanation: The LCA of nodes 2 and 8 is 6.

Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
Output: 2
Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.

Input: root = [2,1], p = 2, q = 1
Output: 2
'''

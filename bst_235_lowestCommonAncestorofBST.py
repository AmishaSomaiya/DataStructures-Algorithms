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

another eg: 7 and 9 : both are > root. so dont need to search in left subtree, only search in 
right subtree. 

so cases :
case 1 : 
if 1 in left subtree and other in right subtree : root is LCA
case 2 :
if both are in 1 subtree, do not search in other subtree
case 3 : 
if one of the nodes is root, then LCA is root

Time Complexity: o(logn) since only visiting 1 node per level = also equal to the height of the
tree and do not need to visit every single node in the tree so not o(n)
space complexity = o(1) since no extra space used 

"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        cur = root  #begin at root
        while cur:  #continue till result achieved which is guaranteed to exist in the input tree
            # so the while condition is while cur
            if p.val > cur.val and q.val > cur.val:  #case1 : both p and q are > root or current value we r visiting:
                # so go down the right subtree
                cur = cur.right  #update current pointer accordingly
            elif p.val < cur.val and q.val < cur.val:  #opposite case
                cur = cur.left
            else:   #last case : split occurs or we found p or q as root/current so return current  
                return cur
            # guaranteed to execute at some point so no return outside of loop needed 
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

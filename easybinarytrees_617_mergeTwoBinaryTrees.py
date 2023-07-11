"""
https://leetcode.com/problems/merge-two-binary-trees/
https://www.youtube.com/watch?v=QHH6rIK3dDQ&list=PLot-Xpze53lfQmTEztbgdp8ALEoydvnRQ&index=16

leetcode 617
easy 
binary trees
 

input : given two binary trees root1 and root2.
output: Return the merged tree.

Logic : 


Time Complexity: 

"""

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1 and not root2:
            return None

        v1 = root1.val if root1 else 0
        v2 = root2.val if root2 else 0
        root = TreeNode(v1 + v2)

        root.left = self.mergeTrees(root1.left if root1 else None, root2.left if root2 else None)
        root.right = self.mergeTrees(root1.right if root1 else None, root2.right if root2 else None)
        return root

'''
Input: root1 = [1,3,2,5], root2 = [2,1,3,null,4,null,7]
Output: [3,4,5,5,4,null,7]

Input: root1 = [1], root2 = [1,2]
Output: [2,2]

'''
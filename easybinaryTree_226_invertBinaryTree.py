"""
https://leetcode.com/problems/invert-binary-tree/
https://www.youtube.com/watch?v=OnSn2XEQ4MY&list=PLot-Xpze53lfQmTEztbgdp8ALEoydvnRQ&index=14

leetcode 226
easy

input : root of a binary tree
output: invert the tree, and return its root.

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
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        if not root:
            return None

        # swap the children
        tmp = root.left
        root.left = root.right
        root.right = tmp

        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
    

'''
testing:
Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]

Input: root = [2,1,3]
Output: [2,3,1]

Input: root = []
Output: []
'''
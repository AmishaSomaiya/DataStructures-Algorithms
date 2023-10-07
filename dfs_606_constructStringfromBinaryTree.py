"""
https://leetcode.com/problems/construct-string-from-binary-tree/    

leetcode 606
easy

input : root of a binary tree
output: construct a string consisting of parenthesis and integers from a binary tree with the preorder traversal way, and return it.

Omit all the empty parenthesis pairs that do not affect the one-to-one mapping relationship between the string and the original binary tree.

Logic : dfs with recursion : preorder traversal

Time Complexity: o(n)

"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
  
    def tree2str(self, root) -> str:        
        res = []
        def dfs(root):
            if not root :
                return
            res.append("(")
            res.append(str(root.val))
            if not root.left and root.right :
                res.append("()")
            dfs(root.left)
            dfs(root.right)
            res.append(")")

        dfs(root)
        return "".join(res)[1:-1]
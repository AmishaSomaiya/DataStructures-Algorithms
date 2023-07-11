"""
https://leetcode.com/problems/validate-binary-search-tree/
https://www.youtube.com/watch?v=s6ATEkipzow&list=PLot-Xpze53lfOdF3KwpMSFEyfE77zIwiP&index=26

leetcode 98
medium
recursive dfs

input : Given the root of a binary tree
output: determine if it is a valid binary search tree (BST)

Logic : 
A valid BST is defined as follows:
The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key. (not >=, strictly >)
Both the left and right subtrees must also be binary search trees.

-so root < all nodes in right subtree : so only checking neighbors is not sufficient

approach1 : recursive brute force : O(n^2)
check root > every value in left and < every value in right 
: needs n comparisons for every node -> O(n^2)

approach2  : recursive dfs : O(2n) = O(n)
- root can be anything between -inf and +inf
-so no need to compare root with anything
-now in left subtree : is -inf < left node < root
-now for right : is root < right < inf
- i.e. not just 1 comparison, update other side bound also updated using -inf or inf
- so for right our condition is root < right < inf
- this should be met for all right
-5(root) < 4(right) < 7(root of right)-> this condition si not met as 5!<4
-so return false. 
Time Complexity: O(n)
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root) -> bool:
        def valid(node, left, right):   #pass node, left and right boundary
            if not node:
                return True  #empty BST = BST so return true 
            if not (left < node.val < right):  #node broke the BST rule so return false 
                return False

            # recursively call dfs down : 
            # parameters to check if left subtree is valid : now we want to check if left node of node is valid for bst
            # so node.left and boundaries : left and right boundary changed to node.val itself because for bst a node < all vals to the right of it (parent)
            # similarly to ensure right sub tree is valid 
            # if both return true then we can finally return true 
            return valid(node.left, left, node.val) and valid(
                node.right, node.val, right
            )

        # initially we will send the root and boundaries as -inf and +inf 
        return valid(root, float("-inf"), float("inf"))
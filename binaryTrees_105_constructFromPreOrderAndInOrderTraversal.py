"""
https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
https://www.youtube.com/watch?v=ihj4IQGZ2zc&list=PLot-Xpze53lfOdF3KwpMSFEyfE77zIwiP&index=24

leetcode 105
medium

input : two integer arrays preorder and inorder where preorder is the preorder traversal of 
a binary tree and inorder is the inorder traversal of the same tree
output: construct and return the binary tree.

Logic : 
-deconstruct pre and inorder traversals and reconstruct the binary tree

-eg : binary tree :
    3
9          20
        15    7

-preorder : root - left - right : [3,9,20,15,7]
-inorder  : left - root - right : [9,3,15,20,7]

reconstruction :
- 1st value of preorder = root -> from preorder
- what will go into left subtree and what into right subtree -> from inorder
- each value in each traversal = unique 

-identify root : 1st node in preorder 
-remove root from preorder and inorder
-everything before root in inorder will go into left subtree, after into right subtree
-repeat recursively 
-since single value 9 in left subtree, done with left
-go back to remaining preorder = [20,15,7] since 3 and then 9 removed
-again 20 is the root from preorder
-from inorder to the left of 20 : 15 is in the left subtree and to the right : 7 : right subtree
-done when preorder and inorder arrays become empty

Time Complexity: 

"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def buildTree(preorder, inorder):
        # base case 
        if not preorder or not inorder:
            return None

        # root is 1st value in preorder
        root = TreeNode(preorder[0])

        # split at root in inorder 
        mid = inorder.index(preorder[0])

        # create left and right subtrees recursively 
        root.left = buildTree(preorder[1 : mid + 1], inorder[:mid])  #pass sublists : new preorder and inorder arrays 
        root.right = buildTree(preorder[mid + 1 :], inorder[mid + 1 :])
        return root

result = buildTree([3,9,20,15,7], [9,3,15,20,7])
print(result)

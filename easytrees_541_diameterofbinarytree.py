"""
https://leetcode.com/problems/diameter-of-binary-tree/

leetcode 543
easy

input : 
output: 

Logic : 


Time Complexity: 

"""

def diameterOfBinaryTree(root):
        res = 0

        def dfs(root):
            nonlocal res

            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            res = max(res, left + right)

            return 1 + max(left, right)

        dfs(root)
        return res

print(diameterOfBinaryTree([1,2,3,4,5]))
print(diameterOfBinaryTree([1,2]))

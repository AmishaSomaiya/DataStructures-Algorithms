"""
https://leetcode.com/problems/count-good-nodes-in-binary-tree/
https://www.youtube.com/watch?v=7cp5imvDzl4&list=PLot-Xpze53lfOdF3KwpMSFEyfE77zIwiP&index=67

leetcode 1488
medium
binary tree

input : a binary tree root, a node X in the tree is named good 
if in the path from root to X there are no nodes with a value greater than X.
output: Return the number of good nodes in the binary tree.

Logic : 
approach 1 : o(n) linear time and space : o(logn) = o(height of tree)

pre-order traversal :
dfs recursively on root-left subtree-right subtree 

first begin with root node : is it a good node : yes
now need to check number of good nodes in left subtree:
so keep a track of largest node so far, before beginning left sub tree
then start from root of left sub tree (preorder traversal):
check if it is good, ie >= greatest value tracked till now on this path 
if yes then add to #good nodes 
continue recursively till end i.e. till all nodes are done 

Time Complexity: 

"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def goodNodes(root: TreeNode) -> int:
        #pass root and maxvalue so far 
        def dfs(node, maxVal):
            # base case 
            # return 0 if null node ie not node 
            if not node:
                return 0

            # now to check if this node is good node or not: 
            # res = 1 if good node 
            res = 1 if node.val >= maxVal else 0
            # update max val so far 
            maxVal = max(maxVal, node.val)
            # run dfs on left and right subchild
            # pass the max value so far 
            res += dfs(node.left, maxVal)  #count the #of good nodes and add to the result so far 
            res += dfs(node.right, maxVal)
            return res  #so finally return the result value
            # so dfs above computes the result 
        return dfs(root, root.val)  #we want to run on entire tree so pass root to call dfs 
# also default value for max value : to be passed above : can be -inf or even root val since root is a good node, it is the max so far 

print(goodNodes([3,1,4,3,None,1,5]))
print(goodNodes([3,3,None,4,2]))
print(goodNodes([1]))
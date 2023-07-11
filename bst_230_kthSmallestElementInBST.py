"""
https://leetcode.com/problems/kth-smallest-element-in-a-bst/
https://www.youtube.com/watch?v=5LUXSvjmGCw&list=PLot-Xpze53lfOdF3KwpMSFEyfE77zIwiP&index=45

leetcode 230
medium
bst, stack 

input : the root of a binary search tree, and an integer k
output: return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

Logic : 
left-root-right 

-put everything in order(sorted array) and return the kth ele
-how to put everything in order(sorted array) from bst :
: go to root(but dont visit it yet)
go to left child : visit it : put it in array
go to right of left sub tree  : visit it: put it in array
then add root : visit, put into array
then go to right sub tree
= inorder traversal for bst recursively

approach : iterative
-start at root (do not visit): add to stack 
-keep going as far left as u can : keep adding to stack
-when null reached : pop from stack : visit it ; incre k 
-other eles added to stack earlier still in stack
-but do not pop more
-continue with inorder traversal ie right of left sub tree 
when null reached then again pop, visit, add to array
when kth ele in array reached : return it 
else when stack is empty: algo is done : all nodes visited 

Time Complexity: same as recursive


"""

from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def kthSmallest(root: Optional[TreeNode], k: int) -> int:
        stack = [] #for iterative approach 
        curr = root #pointer to current node 

        while stack or curr:#loop till stack is not empty or current is not null 
            while curr:  #while current is not null, keep going left : do not visit it yet 
                stack.append(curr) 
                curr = curr.left
            curr = stack.pop()  #when null reached, pop once 
            k -= 1  #decre k 
            if k == 0:  #when k=0, that value : kth ele reached, return it 
                return curr.val
            curr = curr.right  #once popped, can go to right sub tree, repeat till outer while loop 

print(kthSmallest([3,1,4,None,2], 1))
print(kthSmallest([5,3,6,2,4,None,None,1], 3))
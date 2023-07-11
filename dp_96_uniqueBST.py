"""
https://leetcode.com/problems/unique-binary-search-trees/
https://www.youtube.com/watch?v=Ox0TenN3Zpg&list=PLot-Xpze53lfOdF3KwpMSFEyfE77zIwiP&index=31

leetcode 96
medium
dynamic programming 

input : an integer n
output: return the number of structurally unique BST's (binary search trees) which has exactly n nodes of unique values from 1 to n.

Logic : 
nodes, trees
1      1
2      2
3      5

suppose 3 values : 1,2,3
if 1 = root then 2,3 -> right subtree as per defn of bst
such that it can be 1->2->3 with 2 as root of right subtree 
or 1->3->2 with 3 as root of right subtree and 2 as left child of right sub tree
so it does nt matter internally
if 2 = root then 1 in left sub tree, 3 in right sub tree
if 3 = root then 1,2 in left sub tree
= recursive problem, each value can be the root at some point 

so number of bst possible with 1 particular value as root = product of number of trees possible with x as root of left subtree and y as root of right subtree
repeat for all roots and sum it up

eg : 1,2,3,4 #total of 4 nodes
numTree[4] = numTree[0] * numTree[3] + #when root at 1st
             numTree[1] * numTree[2] + #when root at 2nd
             numTree[2] * numTree[1] + #when root at 3rd
             numTree[3] * numTree[1]   #when root at 4th

Time Complexity: O(n^2) since to find for n, need to iterate thru the entire list for each of the n nodes as root 
space : O(n) : to store indiv results for all n 
"""

def numTrees (n):
    # going from 0 to n, initialize an array of 1s of length n+1
    numTree = [1]*(n+1) #for base cases

    # basecase : for 0 or 1 node : 1 tree

    # so loop from 2nd node till end:
    for nodes in range(2, n+1):
        total = 0
        # now consider each node as root node 
        for root in range(1, nodes+1):
            # how many nodes in the left subtree and how many in the right subtree :
            left = root-1
            right = nodes-root
            # then total = sum of product as explained earlier 
            total += numTree[left]*numTree[right]
        # put this total into the cache : numTrees
        numTree[nodes] = total 
        # so find this for nodes = 1 to n 
        # now only return for nodes = n
    return numTree[n]


print(numTrees(3))
print(numTrees(1))



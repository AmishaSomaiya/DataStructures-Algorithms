"""
https://leetcode.com/problems/copy-list-with-random-pointer/
https://www.youtube.com/watch?v=5Y2EiZST97Y&list=PLot-Xpze53lfOdF3KwpMSFEyfE77zIwiP&index=37

leetcode 138
medium
linkedlist
2 pass using hashmap 

input : A linked list of length n is given such that each node contains an additional random pointer, 
which could point to any node in the list, or null.
Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, where each new node has its value set 
o the value of its corresponding original node. Both the next and random pointer of the new nodes should point to new nodes in the copied 
list such that the pointers in the original list and copied list represent the same list state. None of the pointers in the new list 
should point to nodes in the original list.

For example, if there are two nodes X and Y in the original list, where X.random --> Y, then for the corresponding two nodes x and y in 
the copied list, x.random --> y.
The linked list is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:
val: an integer representing Node.val
random_index: the index of the node (range from 0 to n-1) that the random pointer points to, or null if it does not point to any node.

output: Return the head of the copied linked list.

Logic : 
-a regular linkedlist but each node has in addition to next pointer, has an extra pointer : random
-issue : when we deep copy or clone, these random pointers may point to nodes not created yet at that point 
-soln : 2 passes 
-1st pass : create deep copies of the nodes and not link them yet
also : in the 1st pass : create hashmap with mapping from old node to new node 
-2nd pass : pointer connections using hashmap 
Time Complexity: O(n) , s: O(n) for hashmap 

"""
from typing import Optional


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldToCopy = {None: None}  #hashmap to map nodes from old to new 

        #1st pass 
        # cloning nodes and adding to hashmap 
        cur = head
        while cur:  #till curr node becomes null 
            copy = Node(cur.val)  #create copy of this node using Node constructor 
            oldToCopy[cur] = copy  #put this clone/deep copy into the hashmap 
            cur = cur.next  #update current pointer till it reaches null 
        
        #2nd pass 
        # connect the pointers 
        cur = head
        while cur:
            copy = oldToCopy[cur] #since copy already created in hashmap, accessing curr in hashmap will give copy 
            copy.next = oldToCopy[cur.next]  #set both next and random pointers of current to copy 
            copy.random = oldToCopy[cur.random]
            cur = cur.next  #incre current to next till null 
            # edge case : what if curr.next = null, so we want hashmap to return null in that case 
            # hence hashmap inti as {None, None}
        return oldToCopy[head] #return head of copy = head of orig linkedlist and map it to copy


print(copyRandomList([[7,null],[13,0],[11,4],[10,2],[1,0]]))
print(copyRandomList([[1,1],[2,1]]))
print(copyRandomList([[3,null],[3,0],[3,null]]))

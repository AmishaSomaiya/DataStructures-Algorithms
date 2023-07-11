"""
https://leetcode.com/problems/remove-nth-node-from-end-of-list/
https://www.youtube.com/watch?v=XVuQxVej6y8&list=PLot-Xpze53lfOdF3KwpMSFEyfE77zIwiP&index=36

leetcode 19
medium
linkedlist : 2 pointers 

constraint : implement in 1 pass 

input : head of a linked list
output: remove the nth node from the end of the list and return its head.

Logic : 
approach 1 : 
since we do not have end of ll : singly linked list
so reverse the ll and remove the nth node from the beginning
but reversing is unnecessary

approach 2 :
-using 2 pointers : left(at beginning of ll) and right(shifted by n)
-now keep shifting till right at end of list, then left will be at n=2 from end
- so when right points to null, left points to node at n=2 from end 
-remove the node that left-1 is pointing to or use dummy node at beginning (left initialized at dummy instead of beginning node)
-return head = dummy.next 


Time Complexity: O(n)

"""

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeNthFromEnd(head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)  #value doesnt matter, say 0, what is imp is it points to head 
        left = dummy  #initialize left pointer to dummy
        right = head  #initialize right to head+n but need a loop to do that so first init to head

        while n > 0:  #head+n for right pointer 
            right = right.next
            n -= 1

        # once pointers init as above, shift both pointers till right reaches end of list 
        while right:
            left = left.next
            right = right.next

        # once the correct position is reached, delete that node 
        # delete
        left.next = left.next.next
        return dummy.next  #return head 
    

print(removeNthFromEnd([1,2,3,4,5],2))
print(removeNthFromEnd([1],1))
print(removeNthFromEnd([1,2],1))
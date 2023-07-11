"""
https://leetcode.com/problems/linked-list-cycle/

leetcode 141
easy
linkedlist

Logic : fast, slow pointers

input : head of a linked list
output: true if there is a cycle in the linked list

Time Complexity: O(n), Space Complexity: O(1)

"""

from typing import Optional

# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast_pointer = slow_pointer = head

        while fast_pointer and fast_pointer.next:
            fast_pointer, slow_pointer = fast_pointer.next.next, slow_pointer.next
            if fast_pointer == slow_pointer:
                return True

        return False
    

print(Solution.hasCycle([3,2,0,-4]))
print(Solution.hasCycle([1,2]))
print(Solution.hasCycle([1]))
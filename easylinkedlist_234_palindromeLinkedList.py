"""
https://leetcode.com/problems/palindrome-linked-list/
https://www.youtube.com/watch?v=yOzXms1J6Nk&list=PLot-Xpze53lfQmTEztbgdp8ALEoydvnRQ&index=13

leetcode 234
medium

palindrome eg: racecar

input : singly linkedlist
output: determine if it is a palindrome

Logic : 
approach 1 : using extra space 
put into an array ,
use indices and check if palindrome
but this needs extra array

nums = []
while head :
    nums.append(head.val)
    head = head.next

l, r = 0, len(nums)-1
while l<= r :
    if nums[l] != nums[r]:
        return False
    l += 1
    r -= 1
return True 

--

approach 2 : o(1) space 
-2 pointers : slow and fast 
-when fast reaches end, slow will reach the middle
-reverse linkedlist after middle


Time Complexity: 

"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast = head  #2 pointers 
        slow = head
        
        # find the middle (slow)
        while fast and fast.next:  #till fast is at the end of list or at the last node  
            fast = fast.next.next
            slow = slow.next
            
        # reverse second half
        prev = None
        while slow:
            tmp = slow.next
            slow.next = prev
            prev = slow
            slow = tmp
        
        # check palindrome
        left, right = head, prev #prev is last 
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True

"""
testing :
Input: head = [1,2,2,1]
Output: true

Input: head = [1,2]
Output: false   
"""
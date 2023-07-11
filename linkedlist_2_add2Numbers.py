"""
https://leetcode.com/problems/add-two-numbers/

leetcode 2
medium

input : two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, 
and each of their nodes contains a single digit
output: Add the two numbers and return the sum as a linked list

assume the two numbers do not contain any leading zero, except the number 0 itself.

Logic : 
-a lot of edge cases 
-1. if length of both is not equal : assume 0 at the place with missing value 
-2. carry during last addition 
-approach : 
-since nodes are in reverse order, it becomes easier -> start add from 1st node itself 

Time Complexity: 

"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode()  #dummy node and we will return the next of dummy node as resulting linkedlist 
        # so we avoid the edge case of insertion into an empty result linkedlist 
        cur = dummy  #current pointer points to position where we are inserting into the LL


        carry = 0  #initialize
        while l1 or l2 or carry:   #while either 1 has a digit or there is a balance carry (edge case) : 
            v1 = l1.val if l1 else 0  #get digits from both and =0 if there is no digit in 1 but there is in another 
            v2 = l2.val if l2 else 0

            # compute new digit
            val = v1 + v2 + carry  #basic addition 
            carry = val // 10      #in case there is a carry again 
            val = val % 10         #the ones place digit 
            cur.next = ListNode(val)  #insert the value just computed into the next node 

            # update ptrs
            cur = cur.next    #update current pointer to next 
            l1 = l1.next if l1 else None   #update l1 and l2 pointers if there are still digits in them 
            l2 = l2.next if l2 else None

        return dummy.next
    


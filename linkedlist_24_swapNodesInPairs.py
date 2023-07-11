"""
https://leetcode.com/problems/swap-nodes-in-pairs/
https://www.youtube.com/watch?v=o811TZLAWOo&list=PLot-Xpze53lfOdF3KwpMSFEyfE77zIwiP&index=64

leetcode 24
medium
linkedlist 

input : linkedlist head 
output: head after swapping adjacent values
cannot modify values in list's nodes,
only nodes itself may be changed 

Logic : 
go thru every pair and reverse the link 
+ 1st and last should be connected
+ 2nd = now the head 
+ 2ndlast = now the tail

edge cases :
1. we r reversing pairs of nodes 
so last node does nt have a pair to switch link
so loop till second last node 
Time Complexity: looping only once : o(n), space : o(1)

"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def swapPairs(head: ListNode) -> ListNode:
        dummy = ListNode(0, head)  #value = 0 because we dont care about the value and points to head
        prev, curr = dummy, head  #init pointers prev to dummy and curr to head 

        while curr and curr.next:  #loop and reverse till end secondlast since last will not have anything to swap with 
            # save ptrs before changing 
            nxtPair = curr.next.next  #shifting by 2 from current will give next pair 
            second = curr.next  #second node is current.next 

            # reverse this pair
            second.next = curr
            curr.next = nxtPair
            prev.next = second  #second into first position 

            # update ptrs before next iteration, so can reverse next pair 
            prev = curr
            curr = nxtPair

        return dummy.next
    

print(swapPairs([1,2,3,4]))
print(swapPairs([]))
print(swapPairs([1]))



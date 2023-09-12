"""
https://leetcode.com/problems/find-the-duplicate-number/
https://www.youtube.com/watch?v=wjYnzkAhcNk&list=PLot-Xpze53lfOdF3KwpMSFEyfE77zIwiP&index=42

leetcode 287
medium
arrays, 2 pointers, Floyds Algorithm = linkedlist cycle problem 

input : an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.
output: There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and uses only constant extra space.

so constraints :
1. cannot sort inplace (cannot modify the array)
2. need to solve in o(1) space 
Logic : 
approach1 : 
hashset
when repeat value encountered : return it 
-t: O(n) but s:O(n)
-but they have asked for s=O(1)

approach2 :
-length = n+1
-value of each ele = between 1 and n 
-eg : [1,3,4,2,2]  
index: 0,1,2,3,4
0->3->2->4->2 
-consider each value as a pointer :
so 1 points to position 1, 3 points to position 3 and so on
-so if x position points to y and y points back to x : then there is a cycle 
: repeat 
-so begining of a cycle : repeat ele : to be returned 
-also since the range of values = 1 to n, they will never point to index 0 
so index 0 will never be part of the cycle 

-1st step : find the intersection : use fast and slow pointer :
slow pointer from beginning of array till end 1 at a time
fast pointer beginning of array till end 2 at a time
they will intersect somewhere 
find node of intersection
and find the node where both intersect 
-2nd : take 2nd slow pointer at the beginning of the array 
and first slow pointer from point of intersection of fast-slow pointers 
and see if they intersect again : this is the beginning of the cycle = result 

-because as per floyd's : 
distance of beginning of cycle from intersection of slow-fast
= distance of beginning of cycle from the start 

-the pre-portion before the cycle can be really long : can be longer than the cycle itself
then may require multiple passes thru the cycle from the slowpointer1 in the cycle
to intersect(at the beginning of the cycle) with the slowpointer2 coming from the beginning of the list (the preportion)

start of the cycle : where multiple nodes point to single node = repeated node 
= beginning of the cycle = node to be returned

linkedlist problem identified
now apply floyds algo to find the beginning of the cycle
Time Complexity: 

"""

from typing import List


def findDuplicate(nums: List[int]) -> int:
        # phase 1
        slow, fast = 0, 0 #always will start at 0, indexes 
        # and slow and fast will always be in bounds 
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]] #advancing fast twice 
            if slow == fast:  #when intersect: break out of the loop : do while loop 
                break

        # phase 2
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow
            

print(findDuplicate([1,3,4,2,2]))
print(findDuplicate([3,1,3,4,2]))

"""
https://leetcode.com/problems/rotate-array/
https://www.youtube.com/watch?v=BHr381Guz3Y&list=PLot-Xpze53lfOdF3KwpMSFEyfE77zIwiP&index=70

leetcode 189
medium
arrays

input : an integer array nums
output: rotate the array to the right by k steps, where k is non-negative.

Logic : 
rotation:
we want to rotate by i+k
but simply rotating/shifting by i+k will result in eles going out of bounds 
eg : 1,2,3,4,5
for k=2 
to rotate 4 or 5, it will go out of bounds
so soln -> rotate by (i+k) % len(nums)


approach 1 : o(n) time and o(n) space
use extra array and copy back to input array 
but they have asked to rotate in place

approach 2 :
o(n) time and o(1) space

-there are 2 portions in the array : 
the 1st portion (n-k eles) that will go to the end of the array 
the 2nd portion (k eles) that will go to the beginning of the array 

1. reverse the array
2. reverse the 2nd portion which is at the beginning now
3. reverse the 1st portion which is at the end now 


Time Complexity: 
o(1) space 

"""

from typing import List


def rotate(nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # in case  k > len(nums) then need to rotate only k%len times 
        # if k=len then rotate 0 times because rotating len times will give same array back again 
        k = k % len(nums)
        
        # init left and right pointers 
        l, r = 0, len(nums) - 1
        # till pointers have not met or passed each other :
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]  #swap left and right eles in place 
            l, r = l + 1, r - 1  #update pointers 

        # reverse 1st k eles 
        # make helper func and pass diff values for left and right  
        l, r = 0, k - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l, r = l + 1, r - 1

        # reverse remaining eles 
        l, r = k, len(nums) - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l, r = l + 1, r - 1

        print(nums)

rotate([1,2,3,4,5,6,7],3)
rotate([-1,-100,3,99],2)



'''
https://leetcode.com/problems/remove-duplicates-from-sorted-array/submissions/

easy 
3 pointers

input : integer array nums sorted in non-decreasing order
output : remove the duplicates in-place such that each unique element appears only once. 
The relative order of the elements should be kept the same. 
Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. 
The remaining elements of nums are not important as well as the size of nums.
Return k.





'''
from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # 3 pointers
        l = 0
        r = 1
        push = 0
        count = 1

        while r<len(nums):
            if nums[r] == nums[push] :  #keep moving right till dup
                r+=1
            elif nums[r] != nums[push] : 
                #when a new number encountered, push it to l+1, incre count and update pointers 
                push = r
                nums[l+1] = nums[push]
                count+=1
                l+=1
                r+=1

        return count





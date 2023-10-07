"""
https://leetcode.com/problems/binary-search/

leetcode 704
easy
iterative approach

input :  an array of integers nums which is sorted in ascending order, and an integer target
output: 

Logic : write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.


Time Complexity: o(logn)

"""

class Solution:
    def search(self, nums, target: int) -> int:
        # search space is entire array
        l=0
        r=len(nums)-1

        # iterative 
        while(l<=r):
            mid = l + ((r-l)//2) #to avoid overflow

            if nums[mid] == target : #target found 
                return mid
            elif nums[mid] > target : #search left
                r = mid-1
            elif nums[mid] < target : #search right
                l = mid + 1

        # if target not found
        return -1
    


        
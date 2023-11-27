"""
https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
https://www.youtube.com/watch?v=nIVW4P8b1VA&list=PLot-Xpze53lfOdF3KwpMSFEyfE77zIwiP&index=55

leetcode 153
medium

input : an array of length n sorted in ascending order rotated between 1 and n times.
Given the sorted rotated array nums of unique elements.
output: minimum element of this array.

Logic : 
approach1 : 
linear time soln : trverse thru the array and find the min value and return it
but logn time soln required

approach2 : 
given array is sorted in ascending order but can be rotated 1 to n and given
rotation k times means to take the last k elems and put these in front of the remaining n-k elements

to do in logn time : use binary search 
-if sorted array rotated n times:
-left and right pointer 
-find pivot : where 1,2,3,4,5 -> 3,4,5,1,2 so pivot=at 5->1
-but can also take middle as pivot 
now where to search : in left portion of the array or right portion 
: whatever is in the left portion is > whatever in right portion because sorted and rotated
since when rotated : we are putting the large values ahead of the smaller values
so on the right are going to be smaller

so this algo for rotated sorted array : i.e. works only for rotated sorted

where to search :  
if pivot is in the left sorted portion i.e nums[m] >= nums[L]-> search right
else search left

Time Complexity: o(logn)

"""
from typing import List
class Solution:
    def findMin(self, nums: List[int]) -> int:
        # sorted (even though rotated) and need in o(logn) tine so use binary search

        l=0
        r=len(nums)-1
        currmin = float("inf")

        while(l<r):
            mid = (l+r)//2
            currmin = min(currmin, nums[mid])
            if nums[mid]>nums[r]: #right portion
                l=mid+1
            else : #left portion
                r=mid-1

        # if time exceeded, check 1)pointers updated inside loop
        
        # if incorrect answer, 1)check if default return after and outside loop 
        # 2)condition of loop l<r or l<=r

        '''
        bin search flow:
        if target = nums[mid]: return mid
        if target>nums[mid]: (left portion) l=mid+1
        else (target < nums[mid] i.e. right portion) r=mid-1
        '''           
        
        return min(currmin, nums[l])

print(findMin([3,4,5,1,2]))
print(findMin([4,5,6,7,0,1,2]))
print(findMin([11,13,15,17]))

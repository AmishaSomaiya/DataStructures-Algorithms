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


def findMin(nums: List[int]) -> int:
        start , end = 0 ,len(nums) - 1   #start and end pointers 
        curr_min = float("inf")  #init as inf
        
        while start  <  end :   #continue binary search till valid i.e. start < end 
            mid = (start + end ) // 2  
            curr_min = min(curr_min,nums[mid])
            
            # right has the min 
            if nums[mid] > nums[end]:
                start = mid + 1
                
            # left has the  min 
            else:
                end = mid - 1 
                
        return min(curr_min,nums[start])  

print(findMin([3,4,5,1,2]))
print(findMin([4,5,6,7,0,1,2]))
print(findMin([11,13,15,17]))

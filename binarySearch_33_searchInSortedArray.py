"""
https://leetcode.com/problems/search-in-rotated-sorted-array
https://www.youtube.com/watch?v=U8XENwh8Oy8&list=PLot-Xpze53lfOdF3KwpMSFEyfE77zIwiP&index=11

leetcode 33
medium

input : here is an integer array nums sorted in ascending order (with distinct values).
Given the array nums after the possible rotation and an integer target
output: index of target if it is in nums, or -1 if it is not in nums.

rotated : took a pivot, cut into half around the pivot and swapped 
the portions

Logic : 
approach 1: trivial : O(n) 
search thru the array, ele by ele if ele is present in the array 

but Time Complexity: O(log n) required by question 
this time complexity = binary search 
so 3 pointers left, right and mid and consider discrete cases :
if we know we are in the left sorted portion : 
case 1 :  and target > mid, then can eliminate the left 
case 2 : if target < mid and <leftmost value, then eliminae left portion and search in the right portion
case 3 : target < mid but target >=leftmost value then -> run binary search on left and eliminate right 

if we know we are in the right sorted portion of the array :
case 1 : target < mid, search in left 
case 2 : target > mid and also > rightmost, search left
case 3 : target > mid and <= rightmost, search right, eliminate left 

Question :
how to know if we are in left sorted or right sorted portion of the array
ans : if mid >= left, then mid belongs to left sorted portion
else in the right sorted portion 
"""

def search(nums, target):
        l, r = 0, len(nums) - 1  #initialize left and right pointers 

        while l <= r:  #this condition because we can have single value array as well 
            mid = (l + r) // 2  #mid is center
            if target == nums[mid]:
                return mid

            # left sorted portion
            if nums[l] <= nums[mid]: #left value <= mid value
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1
            # right sorted portion
            else:  
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1
        return -1

print(search([4,5,6,7,0,1,2], 0))
print(search([4,5,6,7,0,1,2], 3))
print(search([1], 0))

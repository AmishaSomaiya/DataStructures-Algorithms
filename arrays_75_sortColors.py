"""
https://leetcode.com/problems/sort-colors/
https://www.youtube.com/watch?v=4xbWSRZHqac

leetcode 75
medium
arrays, 3 pointers 

input : array nums with n objects colored red, white, or blue
output: sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

Logic : 
Use three pointers to perform in-place sorting. If nums[mid] is 0, meaning that we need to swap the value in nums[left] and nums[mid] 
to make the array sorted. Another case is that if we encounter 2 in nums[mid], we know that we should swap nusmms[right] and nums[mid] 
to keep the array sorted. By doing so, the array will be sorted in O(n) time after iterating the whole array (worst case).

bucket sort 
Time Complexity: O(n), Space Complexity: O(1)

"""
def sortColors(nums):
        low = 0
        high = len(nums) - 1
        mid = 0

        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid +=1
            else:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1
        return nums

print(sortColors([2,0,2,1,1,0]))
print(sortColors([2,0,1]))

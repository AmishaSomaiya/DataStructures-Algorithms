"""
https://leetcode.com/problems/3sum/

leetcode 
medium
arrays

input : an integer array nums
output: all the triplets [nums[i], nums[j], nums[k]] 
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0

pseudo-code : 
sort the array
declare an empty output list

edge cases : 
1. Since nums are sorted ascendingly,
if nums[i] > 0, then nums[i+1:] are all larger than 0.
Thus, we do not need to check the sum of any triplet equals 0.
i.e. break

2. We do not need to check duplicate triplet : continue

else : to find the sum of two non-duplicate numbers equal target
i+1 <= Search range <= len(nums)-1, previous numbers are searched

Time Complexity: O(n^2), Space Complexity: O(1)

"""

def threeSum(nums):
    nums.sort()
    output_list = []

    for i in range(len(nums)):
        # Since nums are sorted ascendingly,
        # if nums[i] > 0, then nums[i+1:] are all larger than 0.
        # Thus, we do not need to check the sum of any triplet equals 0.
        if nums[i] > 0:
            break

        # We do not need to check duplicate triplet
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        target = -nums[i]                      # We need to find the sum of two non-duplicate numbers equal target
        left, right = i + 1, len(nums) - 1     # i+1 <= Search range <= len(nums)-1, previous numbers are searched

        while left < right:
            total = nums[left] + nums[right]
            # Case 1: find unique triplet that adds up to 0
            if target == total:
                output_list.append([nums[i], nums[left], nums[right]])
                left += 1

                # Drop duplicated triplet
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
            # Case 2: target is bigger than total => we need to make total smaller through moving the right pointer
            elif target < total:
                right -= 1
            # Case 3: target is smaller than total => we need to make total bigger through moving the left pointer
            else:
                left += 1

    return output_list

print(threeSum([-1,0,1,2,-1,-4]))
print(threeSum([0,1,1]))
print(threeSum([0,0,0]))



"""
https://leetcode.com/problems/two-sum/

leetcode 1
easy
arrays

input : an array of integers nums and an integer target
output: indices of the two numbers such that they add up to target

final Logic : Hash Table 
Simply iterate the array and find the target value among the array in each iteration.

# solution 1: brute force 
# target: int, nums: List[int]

 for i in range(len(nums)):
    number_to_find = target - nums[i]
    for j in range(i + 1, len(nums)):
        if nums[j] == number_to_find:
            return [i, j] # Find indices of the two numbers!

Time Complexity for brute force:  O(n^2), Space Complexity: O(1)

solution 2 : using hashmap
declare empty hashmap with keys as array values and values as array indices
this is so because we want to search on array values and return array indices

now loop through the array: 
"""

# Hash Table 

def twoSum(nums, target):
    newdict = {}
    for i, x in enumerate(nums):
        if (target - x) in newdict:
            return [i, newdict.get(target-x)]
        else:
            newdict[x] = i


print(twoSum([2,7,11,15], 9))
print(twoSum([3,2,4], 6))
print(twoSum([3,3], 6))

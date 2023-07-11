"""
https://leetcode.com/problems/contains-duplicate/

leetcode 
easy
arrays, hashset

input : an integer array nums
output: true if any value appears at least twice in the array, 
and return false if every element is distinct

Brute Force
def containsDuplicate(nums: List[int]) -> bool:
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j]:
                return True

    return False
Time Complexity: O(n^2), Space Complexity: O(1)


Improved Solution: Sort
def containsDuplicate(nums: List[int]) -> bool:
    nums.sort()
    left, right = 0, 1
    while right < len(nums):
        if nums[left] == nums[right]:
            return True
        else:
            left, right = right, right + 1

    return False
Time Complexity: O(nlogn), Space Complexity: O(1) 

Optimized Solution: Set or Hash Table
Time Complexity: O(n), Space Complexity: O(n)
"""

def containsDuplicate(nums):
    memo = set()
    for number in nums :
        if number in memo :
            return True
        else:
            memo.add(number)
    return False

print(containsDuplicate([1,2,3,1]))
print(containsDuplicate([1,2,3,4]))
print(containsDuplicate([1,1,1,3,3,4,3,2,4,2]))
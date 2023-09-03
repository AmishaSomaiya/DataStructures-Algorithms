"""
https://leetcode.com/problems/combination-sum/
https://www.youtube.com/watch?v=cQ1Oz4ckceM&list=PLot-Xpze53lfQmTEztbgdp8ALEoydvnRQ&index=4

leetcode 167
2 sum II input array is sorted
medium

input : 1-indexed array of integers numbers that is already sorted in non-decreasing order, target number
output: the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2

The tests are generated such that there is exactly one solution. 
You may not use the same element twice.
Your solution must use only constant extra space.

arrays, 2 pointer

Logic : 
-approach1 : brute force approach O(n^2)
take 1 number, loop on all others and see if this number added to some other number gives the target 

-now since sorted, if sum>target, no need to loop till the end, because sorted, the next numbers added will also be > target


Time Complexity: o(n)

"""

def twoSum(numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        l, r = 0, len(numbers) - 1

        while l < r:
            curSum = numbers[l] + numbers[r]

            if curSum > target:
                r -= 1
            elif curSum < target:
                l += 1
            else:
                return [l + 1, r + 1]
            
print(twoSum([2,7,11,15], 9))
print(twoSum([2,3,4], 6))
print(twoSum([-1,0], -1))

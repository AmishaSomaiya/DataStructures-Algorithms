"""
https://leetcode.com/problems/maximum-subarray/
https://www.youtube.com/watch?v=5WZl3MMT0Eg

leetcode 53
medium

sliding window

input : integer array nums
output: find the (contiguous) subarray with atleast 1 number with the largest sum, and return its sum.

Logic : 
approach 1:
loop on array : start index: 0 to n-1, end index: 0 to n-1 : nested loop, 
third loop k=from i to j -> O(n^3) -> inefficient

approach 2:
save sum of 1 subarray, when we go to the next ele -> just need to add the new ele to this saved sum
-> O(n^2)

approach 3: final approach
do not need to compute every subarray starting at every single value
to find max subarray -> use a shortcut : sliding window 
- remove whenever u get a negative value -> T=O(n), S=O(1)

Time Complexity: O(n)

"""

def maxSubArray(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = nums[0]  #array is nonempty so 0th index value is always going to exist
        # cannot initialize with 0 because there are negative values as well


        total = 0   #current sum
        for n in nums:  #loop on each num in nums
            total += n   #add current num to current sum
            res = max(res, total)
            if total < 0:  #i.e. if prefix = negative, reset current sum to 0
                total = 0
        return res

print(maxSubArray([5,4,-1,7,8]))
print(maxSubArray([1]))
print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
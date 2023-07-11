"""
https://leetcode.com/problems/longest-increasing-subsequence/

leetcode 300
medium

input : integer array nums
output: the length of the longest strictly increasing subsequence

tricky dynamic programming 

Logic : 
subseq : subarray that need not be contiguous 

approach 1 : recursion : brute force dfs
each ele can be included/ not included : 2 choices for each ele
so total possible choices : 2.2.2.2...n times = 2^n
time compl  : O(2^n)

approach 2 : dfs with cache
1. use indices, make a tree, continue if value at any index going forward is > value at that index 
i.e. increasing subseq 
2. caching : LIS of single ele = 1 = cached
3. dp approach : start at last ele and go backward to first index

so LIS[3] = 1
   LIS[2] = max(1, (1+LIS[3] if nums[2]<nums[3]!=true))=1
   LIS[1] = max(1, 1+LIS[2] if nums[1]<nums[2]=true, 1+LIS[3]) =2
   LIS[0] = max(1, 1+LIS[1] or 1+LIS[2] or 1+LIS[3] = max(1,1+1, 1+1, 1+2))=3
Time Complexity: O(n^2) since working backwards 

"""


def lengthOfLIS(nums):
        LIS = [1] * len(nums) #3cache/list initialized to all 1s to cache the repeated work

        for i in range(len(nums) - 1, -1, -1): #2loop in reverse order from last index to 0
            for j in range(i + 1, len(nums)): #loop from i+1 till end of array
                if nums[i] < nums[j]: #1check if subseq is increasing
                    LIS[i] = max(LIS[i], 1 + LIS[j]) #max(itself or 1+LIS[j] = increasing subseq of i : starting at j)
        return max(LIS)

print(lengthOfLIS([10,9,2,5,3,7,101,18]))
print(lengthOfLIS([0,1,0,3,2,3]))
print(lengthOfLIS([7,7,7,7,7,7,7]))


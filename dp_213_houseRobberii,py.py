"""
https://leetcode.com/problems/house-robber-ii/
https://www.youtube.com/watch?v=rWAJCfYYOvM&list=PLot-Xpze53lfOdF3KwpMSFEyfE77zIwiP&index=35

leetcode 213
medium
dp

input : an integer array nums representing the amount of money of each house
All houses at this place are arranged in a circle. 
That means the first house is the neighbor of the last one. 
Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.

output: return the maximum amount of money you can rob tonight without alerting the police.

Logic : 
-same logic as 198-houseRobber but 1st and last ele adjacent houses because of circle

approach here :
1. reuse soln from house robber 1 = helper func 
2. run 1. twice : once on entire array except 1st ele, once on entire array except last ele
3. take max from 2. = result 

Time Complexity: O(n), S: O(1)

"""
from typing import List


def rob(nums: List[int]) -> int:
        # edge cases for circle condition 
        # 2nd : skip 1st, 3rd : skip last 
        # 1 more edge case : what if single ele array : then empty array from 2nd and 3rd 
        # so 1st term = nums[0]
        return max(nums[0], helper(nums[1:]), helper(nums[:-1]))

def helper(nums):  #soln from 198, house robber 1 
        rob1, rob2 = 0, 0

        for n in nums:
            newRob = max(rob1 + n, rob2)  #1st: skip rob2, current=n + rob1=max sum till n-2, 2nd= max till n-1=rob2
            rob1 = rob2
            rob2 = newRob  #in the end, rob2 will contain max from entire array 
        return rob2

print(rob([2,3,2]))
print(rob([1,2,3,1]))
print(rob([1,2,3]))

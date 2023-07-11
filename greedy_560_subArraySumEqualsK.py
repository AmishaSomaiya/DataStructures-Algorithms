"""
https://leetcode.com/problems/subarray-sum-equals-k/
https://www.youtube.com/watch?v=fFVZt-6sgyo&list=PLot-Xpze53lfOdF3KwpMSFEyfE77zIwiP&index=50

leetcode 560
medium
grredy 


input : an array of integers nums and an integer k
output: return the total number of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.

Logic : 
approach 1: bruteforce : O(n^2)
because n^2 diff subarrays in array
start from 1 ele, keep adding 1 ele : find sum 
repeat for all ele
= repeat work 

approach 2 : 
2 pointers, sliding window : not possible because array can have negative values

approach 3 : O(n) : greedy 
hashmap key : prefix sum, value : count of prefix sum how many times occurs
we know sum of subarray and we know k
then if we chop off a prefix such that sum-k = prefix then we get a contig subarray with sum = k 
how to do this : 
1. we want to find if such prefix exists at the beginnning of subarray 
hence maintaining count of prefix
2. cannot count all prefix before building the result : i.e. simult count while building the result 

suppose (1,-1,1,1,1) subarray : sum=3 and k=3 
then 1 subarray is itself and we subtract empty array from it
another subarray : (1,1,1) and subtract prefix(1,-1) => another subarray 

Time Complexity :
    O(N) -> Where N is the size of the array and we are iterating over the array once

Space Complexity:
    O(N) -> Creating a hashmap/dictionary

"""

from typing import List


def subarraySum(nums: List[int], k: int) -> int:
        count = 0  #return result 
        sum = 0  #current sum 
        dic = {}  #hashmap 
        dic[0] = 1 #basecase : single prefix sum that sums to 0 : empty subarray : count =1 
        for i in range(len(nums)):
            sum += nums[i]  #current sum 
            if sum-k in dic:  #if difference in dict then potential addition to result 
                count += dic[sum-k]  #multiple 
            dic[sum] = dic.get(sum, 0)+1 #else if current sum doesnt exist in dict, then give def value of 0, else incre count 
        return count  

print(subarraySum([1,1,1],2))
print(subarraySum([1,2,3],3))




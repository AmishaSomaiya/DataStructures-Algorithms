"""
https://leetcode.com/problems/maximum-alternating-subsequence-sum/
https://www.youtube.com/watch?v=4v42XOuU1XA&list=PLot-Xpze53lfOdF3KwpMSFEyfE77zIwiP&index=73

leetcode 1911
similar to lc 300 
medium
dynamic programming

input : array nums
output: max alternating sum 

Logic : 
if we choose the 1st : +1st, - or skip 2nd, + or skip 3rd etc 
if we skip 1st: +2nd, -3rd etc


approach1: o(2^n) time and memory 

approach 2 : cache : o(b) time and o(1) memory

Time Complexity: 

"""

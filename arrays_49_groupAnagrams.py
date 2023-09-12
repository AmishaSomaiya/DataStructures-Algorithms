"""
https://leetcode.com/problems/group-anagrams/
https://www.youtube.com/watch?v=vzdNOK2oB2E&list=PLot-Xpze53lfOdF3KwpMSFEyfE77zIwiP&index=54

leetcode 49
medium

input : an array of strings strs
output: return in any order : group the anagrams together

Logic : 
approach 1:
anagrams : by rearranging the chars: if u get the same string back
after sorting, anagrams 
Time Complexity: the number of input strs * time to sort each of them :
o(m.nlogn)

approach 2:
each char is from lowercase alphabet : max 26
so count each 
use hashmap
key : pattern : 1e,1a,1t, value : list of strings that have this pattern
time complexity: o(m.n.26) where m=number of strs, n=avg length of the strings,
26=max size of key of hashmap and max length of count array = o(mn) 
space 


"""

from typing import List
from collections import defaultdict


def groupAnagrams(strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list) #default value is ist so dont have to deal with edge case separately 

        for s in strs:
            count = [0] * 26  #count is a list, but lists cannot have keys so change to tuple
            for c in s:
                count[ord(c) - ord("a")] += 1
            ans[tuple(count)].append(s)
        return ans.values()  #we just need values : strs grouped together 

print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
print(groupAnagrams([""]))
print(groupAnagrams(["a"]))     

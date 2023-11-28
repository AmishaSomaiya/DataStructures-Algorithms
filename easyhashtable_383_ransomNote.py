"""
https://leetcode.com/problems/ransom-note/

leetcode 383
easy
hash table

input : two strings ransomNote and magazine
output: boolean

Time Complexity: O(n+m), Space Complexity: O(1), where n is the length 
of ransomNote and m is the length of magazine.

"""
from collections import defaultdict

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        newdict = defaultdict(int)  #remember this should be default dict to avoid handling edge cases of 0 count and not just newdict = {}

        for i in magazine :
            newdict[i] +=1 

        for i in ransomNote :
            if newdict[i] == 0:
                return False
            newdict[i]-=1  #remember to decrement count whenever char encountered in ransomNote 
            
        return True 


print(canConstruct("a","b"))
print(canConstruct("aa","ab"))
print(canConstruct("aa","aab"))



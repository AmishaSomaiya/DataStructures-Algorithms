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

def canConstruct(ransomNote, magazine):
    memo = defaultdict(int)
    for char in magazine:
        memo[char] +=1

    for char in ransomNote:
        if memo[char]==0:
            return False
        
        memo[char]-=1

    return True


print(canConstruct("a","b"))
print(canConstruct("aa","ab"))
print(canConstruct("aa","aab"))



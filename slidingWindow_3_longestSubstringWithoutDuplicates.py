"""
https://leetcode.com/problems/longest-substring-without-repeating-characters/
https://www.youtube.com/watch?v=wiGpQwVHdE0&list=PLot-Xpze53lfOdF3KwpMSFEyfE77zIwiP&index=4

leetcode 3
medium
sliding window, strings

input : string
output: length of longest substring without duplicates

Logic : 
1. check if no duplicates
2. return the longest substring

approach 1:
-begin with 1st char
-check if it has duplicates
-add another char , check if this new substring has duplicates, then check if it is the longest
-after reaching end of string, repeat the same for char starting at second position

approach 2: sliding window
-avoid repeat work :
-if 1 substring has duplicates, all subsequent substrings beginning at that position will also have duplicates
-so for a particular starting position, once a duplicate is encountered, can just stop there, no need to 
proceed to check other subseqs beginning at that starting position
-when a duplicate is encountered, keep shrinking window from the left till dup is removed

Time Complexity: O(n), space comp: O(n) for the set

"""

def lengthOfLongestSubstring(s):
        charSet = set()
        l = 0   #left pointer initialized to 0
        res = 0 #init result

        for r in range(len(s)): #right pointer will iterate thru the string
            while s[r] in charSet:  #while a duplicate is encountered, keep doing till duplicates are in the set
                charSet.remove(s[l])  #update window and set, left pointer
                l += 1
            charSet.add(s[r])  #after all dups are removed, add the rightmost char to the set
            res = max(res, r - l + 1)  #now that substr does not have dups, update result
        return res #after looping thru entire string

print(lengthOfLongestSubstring("abcabcbb"))
print(lengthOfLongestSubstring("bbbbb"))
print(lengthOfLongestSubstring("pwwkew"))


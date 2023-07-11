"""
https://leetcode.com/problems/valid-anagram/

leetcode 242
easy
strings, hashmap

input : two strings s and t
output: rue if t is an anagram of s, and false otherwise

Logic : 
approach 1 : count occurrences of each char in both s and t and if they are equal, they are anagrams
using hashmap : key value pair : char and count
first fill both hashmaps, then iterate thru 1 and compare ele-wise to another
if all are true then true

Time Complexity: O(s+t) since have to iterate thru both s and t
Space complexity : O(s+t) since building hashmaps

followup : change to O(1) space complexity
-> solution 2: 
-> sort both and if anagrams then after sorting should be the same
-> O(1) space but sorting will need O(nlogn)time
"""

def isAnagram(s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        if len(s) != len(t): #then not a palindrome -> return F directly 
            return False

        # to count occurrence of each char in each string s and t 
        countS, countT = {}, {} #hashmaps for both s and t

        for i in range(len(s)): #loop on length of either s or t = same
            countS[s[i]] = 1 + countS.get(s[i], 0)  #s[i] = char at index i = key of hashmap
            # not using 1+countS(s[i]) because it will throw error if key doesnt exist
            # so use countS.get(s[i]) instead 
            # and countS.get(s[i],0) : default value of 0 because if key doesnt exist in hashmap, just give it 
            # value of 0 by default
            countT[t[i]] = 1 + countT.get(t[i], 0)
        
        # return below same as 
        # second loop
        # for c in countS:
        #   if countS[c] != countT.get(c,0)
        #       return False
        # return True

        return countS == countT

        # solution 2:
        # return sorted(s)==sorted(t)


print(isAnagram("anagram","nagaram"))
print(isAnagram("rat","car"))


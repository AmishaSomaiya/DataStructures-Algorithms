"""
https://leetcode.com/problems/valid-palindrome-ii/

leetcode 680
easy
2 pointer 

input : Given a string s
output: return true if the s can be palindrome after deleting at most one character from it.

Logic : 2 pointers, skip left and right, check if rest is palindrome

Time Complexity: o(n)

"""

class Solution:
    def validPalindrome(self, s: str) -> bool:
        l,r = 0, len(s)-1

        while(l<r):
            if s[l]==s[r]:
                l+=1
                r-=1
            else :
                return self.checkpalin(s,l+1,r) or self.checkpalin(s,l,r-1)
        return True
    
    def checkpalin(self,s,l,r):
        while l<r:
            if s[l] == s[r]:
                l+=1
                r-=1
            else :
                return False
        return True
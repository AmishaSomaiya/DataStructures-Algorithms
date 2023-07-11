"""
https://leetcode.com/problems/longest-palindromic-substring/

leetcode 5
medium

input : string s
output: the longest palindromic substring in s

Logic : 
approach 1 : brute force 
- beginning from first char : keep adding 1 char, and check if it is a palindrome
- repeat for all chars as the beginning char 
Time Complexity: n time to check if substring and checking for n^2 substrings so O(n^3)
- in this approach : palindrome from outside to in

approach 2 :
- check palindrome from inside to outside 
- so now we loop on the string and consider the current char as the centre of potential palindrome
- so beginning with the first char : b : there is nothing to the left of it : so with this b as center, it cannot be a palindrom
- next is a : consider a as centre, there is b to the left and right : palindrome = equal
- so the longest palindrome with a as center = length 3 = bab
- so consider each char as center and expand outwards
= n chars and expanded outwards for each char = n so n^2
-> O(n^2)
-edge case : the above approach will only give palindromes of odd length
so even lengthed string = edge case 

"""

def longestPalindrome(s):
        res = ""  #good default case to return : empty string
        resLen = 0  #longest length initially = 0

        for i in range(len(s)):  #loop through each position in the string as center
            # odd length
            l, r = i, i   #left and right pointers, initialized to center
            while l >= 0 and r < len(s) and s[l] == s[r]:  #inbound and palindrome
                if (r - l + 1) > resLen:  #(r - l + 1) len of current palindrome > current longest length
                    res = s[l : r + 1]  #then update the result
                    resLen = r - l + 1  #and the reuslt length
                l -= 1   #expand the pointers outwards 
                r += 1

            # even length
            l, r = i, i + 1   #pointers initialized differently, rest is the same
            while l >= 0 and r < len(s) and s[l] == s[r]:
                # if inside while : imp
                if (r - l + 1) > resLen:
                    res = s[l : r + 1]
                    resLen = r - l + 1
                l -= 1
                r += 1

        return res

print(longestPalindrome("babad"))
print(longestPalindrome("cbbd"))

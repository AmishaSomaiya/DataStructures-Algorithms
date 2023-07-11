"""
https://leetcode.com/problems/palindromic-substrings/
https://www.youtube.com/watch?v=4RACzI5-du8&list=PLot-Xpze53lfOdF3KwpMSFEyfE77zIwiP&index=46

leetcode 647
similar to leetcode 5 : longest palindromic substring 
medium
strings

input : string s
output: return the number of palindromic substrings in it

A string is a palindrome when it reads the same backward as forward.
A substring is a contiguous sequence of characters within the string.
can be odd lengthed or even lengthed 
Logic : 
approach 1 : brute force : O(n^3)
-thru every single substring : have 2 pointers : at beginning and end of substring
keep comparing and move inwards, if it is true, then add 1 to result 
so n^2 substrings and finding if palindrome for each : n so total o(n^3) time complexity for brute force 

approach 2: inside out : optimized : O(n^2), space : o(n^2)
check inside out like lc #5 
consider char as middle and go both ways outside 
we know middle portion is already pali, if left and right are equal, 
then 1 more palin added, incre count, shift pointers, and we cut down on repeated work 
if not equal, change middle char 

Time Complexity: O(n^2), space : o(n^2) 
easy code 
"""

def countSubstrings(s: str) -> int:
        res = 0  #to return count 

        for i in range(len(s)):
            res += countPali(s, i, i)  #for odd length pali
            res += countPali(s, i, i + 1)  #for even length pali 
        return res

def countPali(s, l, r):  #s:string, l,r = pointers init as i 
        res = 0
        while l >= 0 and r < len(s) and s[l] == s[r]:  #1st, 2nd conditions : in bound check, 3rd : if equal  
            res += 1  #then palindrome found 
            l -= 1    #update pointers 
            r += 1
        return res

print(countSubstrings("abc"))
print(countSubstrings("aaa"))
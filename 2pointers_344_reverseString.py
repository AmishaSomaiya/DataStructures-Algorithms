"""
https://leetcode.com/problems/reverse-string/

leetcode 344
easy
2 pointers

input : input string is given as an array of characters s.
output: Write a function that reverses a string. You must do this by modifying the input array in-place with O(1) extra memory.

Logic : 
Approach 1 : using stack but o(n) space 
Approach 2 : using recursion but o(n) space
Approach 3 : using 2 pointers o(1) space 

Time Complexity: o(n)
space : o(1)

"""
# approach 1
class Solution1:
    def reverseString(self, s) -> None:
        stack = []
        for i in s:
            stack.append(i)

        i=0
        while stack :
            s[i]= stack.pop()
            i+=1

# approach 2
class Solution2:
    def reverseString(self, s) -> None:
        def reverse(l,r):
            if l<r:
                s[l], s[r] = s[r], s[l]
                reverse(l+1, r-1)
        
        reverse(0,len(s)-1)


class Solution:
    def reverseString(self, s) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l,r = 0, len(s)-1
        while l<r:
            s[l], s[r] = s[r], s[l]
            l+=1
            r-=1
            
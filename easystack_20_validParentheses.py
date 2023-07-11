"""
https://leetcode.com/problems/valid-parentheses/
https://www.youtube.com/watch?v=WTzjTskDFMg&list=PLot-Xpze53lfQmTEztbgdp8ALEoydvnRQ&index=12

leetcode 20
easy
stack or python list

input : 
output: 

Logic : 


Time Complexity: 

"""

def isValid(s):
        Map = {")": "(", "]": "[", "}": "{"}  #hashmap for all bracket pairs
        stack = []

        for c in s:  #loop on input string     
            # if c is closing parentheses (all keys of map)
            if c in Map:
            # and stack is not empty since we cant add closing to empty stack 
            # and value at top of stack is matching opening 
                if stack and stack[-1] == Map[c]:
                    stack.pop()
                else:  
                    return False
            else : #else if it was an opening parentheses then just add to stack
                stack.append(c)
        return True if not stack else False

print(isValid("()"))
print(isValid("()[]{}"))
print(isValid("(]"))



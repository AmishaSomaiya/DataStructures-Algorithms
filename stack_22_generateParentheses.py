"""
https://leetcode.com/problems/generate-parentheses/
https://www.youtube.com/watch?v=s9fokUqJ76A&list=PLot-Xpze53lfOdF3KwpMSFEyfE77zIwiP&index=12

leetcode 22
medium
stack 

input : n pairs of parentheses
output: generate all combinations of well-formed parentheses.

Logic : 
not possible : )(

approach 1 : backtracking bruteforce 
1. cannot start with a close parenthese
2. so start with open
now next can be open or closed any
keep count of open and close
can add close only if #close < #open
can add open only if #open < n
3. iff the #open = #close = n then = base case , limit reached 



"""

def generateParenthesis(n):
        stack = []  #to hold parentheses
        res = [] #to hold list of valid parentheses

        def backtrack(openN, closedN):  
            if openN == closedN == n:  #base case, take every char from stack, join them together into an empty string, append to result, return
                res.append("".join(stack))
                return

            if openN < n: # #open < n
                stack.append("(") #append an open parentheses
                backtrack(openN + 1, closedN) #continue backtrack but incre open count by 1
                stack.pop() #after backtrack, update stack : global var 
            if closedN < openN:
                stack.append(")")
                backtrack(openN, closedN + 1)
                stack.pop()

        backtrack(0, 0) #backtrack func defined above, call backtrack function with 0,0 = initial 0,0 count for #open and #closed 
        return res

print(generateParenthesis(3))
print(generateParenthesis(1))





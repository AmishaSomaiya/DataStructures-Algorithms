"""
https://leetcode.com/problems/climbing-stairs/
https://www.youtube.com/watch?v=Y0lT9Fck7qI&list=PLot-Xpze53lfQmTEztbgdp8ALEoydvnRQ&index=9

leetcode 70
easy

input : n steps to reach the top. Each time you can either climb 1 or 2 steps. 
output: In how many distinct ways can you climb to the top?

dynamic programming

Logic : 


Time Complexity: o(n) 

"""

class Solution:
    def climbStairs(self, n: int) -> int:

        if n<=3:
            return n

        n1 = 2
        n2 = 3

        for i in range(4,n+1): #remember till n+1 
            temp = n1+n2
            n1 = n2
            n2 = temp

        return n2 #this is n2 and not temp

print(climbStairs(2))
print(climbStairs(3))


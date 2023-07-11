"""
https://leetcode.com/problems/counting-bits/
https://www.youtube.com/watch?v=RyBM56RIWrM&list=PLot-Xpze53lfOdF3KwpMSFEyfE77zIwiP&index=58

leetcode 338
medium
dp

input : an integer n
output: eturn an array ans of length n + 1 such that 
for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.

Logic : 
bruteforce : nlogn 
-take mod2 : take 1s place, if 1 add it to result
-divideby2 : so remove the last digit and consider the rest of digits other than last digit :
and repeat 
when number/2 = 0 : stop 

approach : linear o(n)
binary repre :
0 - 0000 - 0
1 - 0001 - 1
2 - 0010 - 1
3 - 0011 - 2
---
4 - 0100 
5 - 0101 
6 - 0110
7 - 0111
8 - 1000
now from 4 to 7 = (same as 0 to 3) + 1
i.e. dp[4]= 1 + dp[0] etc
i.e. dp[n]= 1 + dp[n-4]

now fro 8 = 1 + dp[n-8] i.e. dp[n-offset]
where offset = most significant bit so far 
= [1,2,4,8,16] = power of 2

base case => dp[0] = 0
1 -> dp[1] = 1 + dp[n-1]  //msb=1
2 -> dp[2] = 1 + dp[n-2]  //msb=2
3 "
4 -> new power of 2 -> dp[4] = 1 + dp[n-4]
5,6,7 "
8 -> dp[8] = 1 + dp[n-8]



Time Complexity: o(n) linear, space : o(n) for dp array 

"""

from typing import List


def countBits(n: int) -> List[int]:
        dp = [0] * (n + 1)  #dp array init to all 0s of length n+1 
        offset = 1 #= highest power of 2 so far, initial offset 2^0 : 1

        for i in range(1, n + 1):  #to iterate from 1 to n 
            if offset * 2 == i: #check if next power of 2 reached 
                offset = i  #then set i as offset 
            # else offset remains the same
            # in any case, dp calc as follows : 
            dp[i] = 1 + dp[i - offset]
        return dp

print(countBits(2))
print(countBits(5))


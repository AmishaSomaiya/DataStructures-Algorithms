"""
https://leetcode.com/problems/minimum-number-of-swaps-to-make-the-string-balanced/description/
https://www.youtube.com/watch?v=3YDBT9ZrfaU&list=PLot-Xpze53lfOdF3KwpMSFEyfE77zIwiP&index=57


leetcode 1963
medium
strings 

input :  a 0-indexed string s of even length n. 
The string consists of exactly n / 2 opening brackets '[' and n / 2 closing brackets ']'.
A string is called balanced if and only if:

It is the empty string, or
It can be written as AB, where both A and B are balanced strings, or
It can be written as [C], where C is a balanced string.
You may swap the brackets at any two indices any number of times.

output: Return the minimum number of swaps to make s balanced.

Logic : 
edge cases : 1st brac cannot be closed : needs swaps
we dont have to swap, just count the number of swaps required
2. we check by #close !> #open 
i.e. track #extra close brackets needed
=> min number of swaps 

init extra close = -1 
+ (-1) if open encountered
+ (+1) if close encountered

when extra close = 0 -> balanced

the max number of extra close ! to be returned because 
with 1 swap 2 brackets are balanced

so instead return (max + 1) // 2, // for integer division 

Time Complexity: single pass : linear o(n) and space : o(1)

"""

def minSwaps(s: str) -> int:
        extraClose, maxClose = 0, 0  #2 vars, both init to 0

        for c in s:
            if c == "[":  #as discussed above 
                extraClose -= 1
            else:
                extraClose += 1

            maxClose = max(maxClose, extraClose)  #at every iteration 

        return (maxClose + 1) // 2  # Or math.ceil(maxClose / 2)

print(minSwaps("][]["))
print(minSwaps("]]][[["))
print(minSwaps("[]"))


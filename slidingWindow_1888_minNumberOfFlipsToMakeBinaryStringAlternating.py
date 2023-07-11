"""
https://leetcode.com/problems/minimum-number-of-flips-to-make-the-binary-string-alternating/
https://www.youtube.com/watch?v=MOeuK6gaC2A&list=PLot-Xpze53lfOdF3KwpMSFEyfE77zIwiP&index=62

leetcode 1888
medium
sliding window

input : a binary string s. 
You are allowed to perform two types of operations on the string in any sequence:
Type-1: Remove the character at the start of the string s and append it to the end of the string.
Type-2: Pick any character in s and flip its value, i.e., if its value is '0' it becomes '1' and vice-versa.

output: Return the minimum number of type-2 operations you need to perform such that s becomes alternating.
The string is called alternating if no two adjacent characters are equal.
For example, the strings "010" and "1010" are alternating, while the string "0100" is not.
 
Logic : approach1 : o(n^3)
type 2 operation -> take prefix and move to the end 
if eg 1100 -> flipped once -> 1001 -> 0011
flipped n times -> input string again

approach2 : o(n^2)
using type 1 operation 
repeated work 

approach3 : o(n) linear time 
implemented as follows 


Time Complexity: 

"""

def minFlips(s):
    #size of window : length of input string 
    n = len(s)
    # add it to itself 
    s = s + s
    #2 alternating strings, starting with 0 or starting with 1 : target strings
    alt1, alt2 = "", ""
    # length of both of these = same = twice length of orig
    # get values
    for i in range(len(s)):
        # add 0 if even number or else add 1
        alt1 += "0" if i % 2 else "1"
        # opposite for alt2
        alt2 += "1" if i % 2 else "0"

    # initialize result array with def value length of s or float infinity
    # start out with a big number, ultimately trying to flip 
    res = len(s)
    # track of number of differences / flips in alt2 and alt2
    diff1, diff2 = 0,0
    # sliding window: left pointer at 0 
    # and right pointer iterating thru every single position in s
    l = 0
    for r in range(len(s)):
        # for every single char:
        # at curr char r : if it is different from the alt1 same position r
        if s[r] != alt1[r]:
            # then incre different count
            diff1 += 1
        # similarly for alt2 :
        if s[r] != alt2[r]:
            diff2 += 1
        # if window size is too big i.e. > n : 
        # then decrement the left pointer
        # but update diff1 and diff2 before that 
        if (r-l+1) > n :
            # if there is a difference:, decre diff1 count
            if s[l] != alt1[l]:
                diff1 -= 1
            # similarly for diff2
            if s[l] !=alt2[l]:
                diff2 -= 1
            l += 1

            # update result only if window size exact = n
            if (r-l+1) == n:
                res = min(res, diff1, diff2)

    return res 


print(minFlips("111000"))
print(minFlips("010"))
print(minFlips("1110"))








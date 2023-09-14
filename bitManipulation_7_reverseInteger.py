"""
https://leetcode.com/problems/reverse-integer/
https://www.youtube.com/watch?v=HAgLH58IgJQ&list=PLot-Xpze53lfQmTEztbgdp8ALEoydvnRQ&index=17

leetcode 7 
medium
bit manipulation 


input :  a signed 32-bit integer x
output: return x with its digits reversed. 
If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], 
then return 0.
Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

Logic : 
use integer division and mod operators to extract digit by digit from the original number
and then to revere it, multiply extracted digit by 10 to shift by 1 position to the left and 
add the new extracted integer.
repeat till input integer is != 0

to handle the edge case : i.e. to not go out of bounds :
compare the newly formed number with the 32-bit int min and max values (it 1 less digit) 
and if it exceeds, return 0
if it is same, check last digit, if it exceeds return 0



Time Complexity: o(log|x|) space : o(1)  

"""



import math


def reverse(x: int) -> int:
             # Integer.MAX_VALUE = 2147483647 (end with 7)
        # Integer.MIN_VALUE = -2147483648 (end with -8 )

        MIN = -2147483648  # -2^31,
        MAX = 2147483647  #  2^31 - 1

        res = 0
        while x:  #i.e. while integer x is not zero, continue the while loop
            digit = int(math.fmod(x, 10))  # (mod operation in python),  -1 %  10 = 9
            x = int(x / 10)  # (python integer division, casting rounds down) -1 // 10 = -1

            #comparing for overflow 
            if res > MAX // 10 or (res == MAX // 10 and digit > MAX % 10): #last and condition : 7
                return 0
            if res < MIN // 10 or (res == MIN // 10 and digit < MIN % 10):  #last and condition : 8
                return 0
            res = (res * 10) + digit
        #return result if it does not overflow 
        return res

print(reverse(123))
print(reverse(-123))
print(reverse(120))

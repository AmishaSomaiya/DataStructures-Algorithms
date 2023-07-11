"""
https://leetcode.com/problems/multiply-strings/
https://www.youtube.com/watch?v=1vZswirL8Y8&list=PLot-Xpze53lfOdF3KwpMSFEyfE77zIwiP&index=51

leetcode 43
medium

input : Given two non-negative integers num1 and num2 represented as strings
output: return the product of num1 and num2, also represented as a string.

You must not use any built-in BigInteger library or convert the inputs to integer directly.

Logic : 
-nums1 and 2 can be xtremely large so written as strings
-cannot convert directly to int and multiply
-2 parts :
1. how to multiply numbers
2. how to translate to strings

-carry also inplace added instead of separate variable
-position : sum of indices of both numbers
because 123 x 456 -> so it is not 1x6 but 100x6

-number of digits in output can be > number of digits in input 
max sum of number of digits of both 

-preallocate output array and convert it to string 
-start from right most : ie in the reverse order so ones position will be leftmost in output
so convert to string in reverse order 

mod10-> ones place
divideby10 -> carry 

Time Complexity: O(n.m), space : O(n+m) because additional array 

"""

def multiply(num1: str, num2: str) -> str:
        if "0" in [num1, num2]:  #if any 1 number = 0, return 0
            return "0"

        res = [0] * (len(num1) + len(num2))  #length of result array 
        num1, num2 = num1[::-1], num2[::-1]  #reverse each number before processing 
        for i1 in range(len(num1)):  #i1 : pointer for num1, i2 : pointer for num2 
            for i2 in range(len(num2)):
                digit = int(num1[i1]) * int(num2[i2]) #convert to int to multiply
                res[i1 + i2] += digit  #in case 2 digit number : needed to do this 
                res[i1 + i2 + 1] += res[i1 + i2] // 10  #carry
                res[i1 + i2] = res[i1 + i2] % 10  #ones place 

        res, beg = res[::-1], 0  #reverse, to get rid of leading zeroes 
        while beg < len(res) and res[beg] == 0:  #incre pointer till leading zeroes 
            beg += 1
        res = map(str, res[beg:])  #array to string 
        return "".join(res)

print(multiply("2", "3"))
print(multiply("123", "456"))
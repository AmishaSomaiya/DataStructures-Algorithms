"""
https://leetcode.com/problems/letter-combinations-of-a-phone-number/
https://www.youtube.com/watch?v=0snEunUacZY

leetcode 17
medium
recursion, backtracking 

input : string containing digits from 2-9 inclusive
output: return all possible letter combinations that the number could represent in any order

Logic : 
-will need to hard-code the characs since for eg 7 has 4 characs
-each digit -> say 2 -> abc so -> a,b,c then followed by say 3 -> a followed by d,e,f then b followed
by d,e,f then c followed by d,e,f and so on. 

pseudo-code : 
- empty list res = [] to contain the combination strings to output
- create a map of digits : hardcoded
-now write the backtracking function : recursive function : arguments 1.)the index i : at what index
are we in the input digit string 2.)currentstring
-base case : if index >= len(digits) i.e. len(currentstring) is exactly = len(digits), -> we have 
taken 1 character from each digit of digits -> then append current string to result and return
-if not -> current string is not completely built yet 
-> loop on every char in the str of the digit corres to that digit i.e.
for c in digitToChar[digits[i]]: -> recursively call backtrack with args : 1.) increment index by 1
since now visiting next index 2.)currentstring + c(current char corresponding to current string)
-last, call this backtrack function with args 1.) index=0, currentstring="" initially empty
-call backtrack func only if digits not empty
-if digits is empty, return empty array hence above condition
-finally return result






Time Complexity: O(4^n), Space Complexity: O(n), where n is the length of array 
O(n4^n) because number of different outputs we can have = 4 to the power n  and len(out) = len(in) = n
thus, O(n4^n) -> wprst case time complexity

"""
def letterCombinations(digits):
    res = []
    digitToChar = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "qprs",
        "8": "tuv",
        "9": "wxyz",
    }

    def backtrack(i, curStr):
        if len(curStr) == len(digits):
            res.append(curStr)
            return
        for c in digitToChar[digits[i]]:
            backtrack(i + 1, curStr + c)

    if digits:
        backtrack(0, "")

    return res


print(letterCombinations("23"))
print(letterCombinations(""))
print(letterCombinations("2"))
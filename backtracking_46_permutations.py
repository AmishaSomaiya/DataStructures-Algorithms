"""
https://leetcode.com/problems/permutations/
https://www.youtube.com/watch?v=s7AvT7cGdSo&list=PLot-Xpze53lf5C3HSjCnyFghlW0G1HHXo&index=2

leetcode 46
medium
recursion, backtracking

input : array nums of distinct integers
output: all the possible permutations in any order.

Logic : 
- base case : single digit for eg 3 -> all permutations are the same number itself
- go 1 level up -> 

Time Complexity: O(n*n!), Space Complexity: O(n), where n is the length of array
"""
def permute(nums):
        res = []  #to output the result

        # base case
        if len(nums) == 1: #return list of lists even if only 1 value
            return [nums[:]]  #faster than nums.copy() =  nums[:] is a deep copy

        # loop on nums for eg : 123
        for i in range(len(nums)):
            n = nums.pop(0)  #pop the first value : for eg 1
            perms = permute(nums) #find permuations of remaining values for eg 23: recursive call

            # now go thru each permutation, append the first value that we removed for eg 1
            for perm in perms:
                perm.append(n)
            res.extend(perms)  #add the final permutation to the result
            nums.append(n)     #clean up what we just did, we removed 1 so add it back 
        return res  #once all permutations are ready : return result 


print(permute([1,2,3]))
print(permute([0,1]))
print(permute([1]))


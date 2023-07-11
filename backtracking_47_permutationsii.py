"""
https://leetcode.com/problems/permutations-ii/
https://www.youtube.com/watch?v=qhBVWf0YafA&list=PLot-Xpze53lfOdF3KwpMSFEyfE77zIwiP&index=20


leetcode 47
medium
backtracking 

input : a collection of numbers, nums, that might contain duplicates
output: return all possible unique permutations in any order.

Logic : 
since duplicates contained but not allowed -> a normal decision tree wont work :
eg : 1,1,2 so a normal decision tree will have 3 branches starting from 1, 1 and 2
but that will result into a duplicate because begins extactly by same 1 in both 1st and 2nd branch
which is not allowed : so this approach will not work

approach :
instead of array as input, use hashmap as input
hashmap : ele, count of ele
so modified decision tree : number of branches : number of keys of hashmap
and reduce count as that ele is used in the tree
then now we wont have 3 decision branches but rather only 2 : even though 112 but tree : 12
-number of choices = number of available counts in hashmap 


Time Complexity: O(n2^n) or O(n!) to be confirmed 

"""
from collections import Counter

def permuteUnique(nums):
        res = []
        perm = []
        count = {n:0 for n in nums} #hashmap 
        for n in nums :
            count[n] += 1

        def dfs():
            if len(perm)== len(nums): #base case 
                    # update every time there is a changed list created till length (completed)
                    res.append(perm.copy()) #copy because perm will be overwritten 
                    return
              
            #   brute force : backtracking
            for n in count:  #count is hashmap so every key is unique 
                if count[n] > 0:  #enough values left: allowed to choose for a permutation 
                      perm.append(n) #add this value to current permutation 
                      count[n] -= 1  #corresponding count decrement by 1

                      dfs() #recursively call dfs again
                    #   will return when base case reached 

                    # cleanup to ensure no duplicates 
                      count[n] +=1
                      perm.pop()
            
        dfs() #call dfs
        return res 

print(permuteUnique([1,1,2]))
print(permuteUnique([1,2,3]))












#         approach 2
        # result = [] #list of perms of output
        # counter = Counter(nums)
# 
        # def backtrack(perm, counter):
        #     if len(perm) == len(nums):
        #         result.append(perm.copy())

        #     for n in counter:
        #         if counter[n] == 0:
        #             continue
        #         perm.append(n)
        #         counter[n] -= 1
        #         backtrack(perm, counter)
        #         perm.pop()
        #         counter[n] += 1

        # backtrack([], counter)  #perm: single var initialized to empty
        # # a list to store each permutation itself 

        # return result



"""
https://leetcode.com/problems/subsets/
https://www.youtube.com/watch?v=REOH22Xwdkk

leetcode 78
medium
arrays, backtracking 

input : an integer array nums of unique elements
output: return all possible subsets (the power set) in any order without duplicates

Logic : [1,2] same as [2,1] so return 1 of these only
-irresp of what is given , empty subset will always be part of it
-choice to include/exclude each ele = 2 choices for each ele -> total number of subsets = 2^n 


pseudo-code : 
-begin with an ele -> add and not add
-go to next ele -> add and not add
-repeat 

Time Complexity: O(n*2^n), Space Complexity: O(n), where n is the length of array   

"""

def subsets(nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []  #result list to add subsets

        subset = []  #array ds to build subset

        def dfs(i):  #dfs function, i = index of ele currently visiing
            if i >= len(nums):  #base case : out of bounds then just return 
                res.append(subset[:]) #that means we have passed the leaf node -> append this to output and return
                return
            # 2 decisions
            # decision to include nums[i]
            subset.append(nums[i])
            dfs(i + 1)  #left branch recursive call on i+1
            # decision NOT to include nums[i]
            subset.pop()  #to not include and then run dfs
            dfs(i + 1)

        dfs(0)
        return res

print(subsets([1,2,3]))
print(subsets([0]))
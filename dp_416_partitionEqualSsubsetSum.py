"""
https://leetcode.com/problems/partition-equal-subset-sum/
https://www.youtube.com/watch?v=IsvocB5BJhw&t=625s

leetcode 416
medium
dynamic programming

input : an integer nonempty array nums (only positive ints)
output: true if you can partition the array into two subsets such that the sum of the elements in
both subsets is equal or false otherwise

Logic : 
subset sum = half and sum of remaining eles = half as well

pseudo-code : 
approach 1 : brute force :
every ele -> choose or not choose in the subset sum and check sum = half or not
if >half : do not go on that path -> stop on that path
if =half : target found : no need to go further -> stop on that path
eg : [1, 5, 11, 5]
make a tree pick 1 or not : then in each branch pick 5 or not and so on
O(2^n)

approach 2: DFS backtracking + cache 
cut down on repeat work :
eg : [1, 5, 11, 5]
first ele : 1 now on the branch where 1 is selected, new target sum needed = (11-1)=10 and not 11 
so now a new sub prob with target 10 : so now looking at sub array [5, 11, 5]
and not looking at complete array anymore, so start index increased by 1
Time Complexity = Space Complexity = O(n.sum(nums)) where sum(nums)=size of cache

approach 3 : DP
start with 1 value, know sum of subset (i.e. everything other than that element)
space complexity becomes O(sum(nums))
"""

def canPartition(nums):
        if sum(nums) % 2:  #cannot partition into half, so return false
            return False

        dp = set()
        dp.add(0)  #base case of 0 : guaranteed to attain sum of 0 if we dont choose any element 
        target = sum(nums) // 2 #target is half of sum

        for i in range(len(nums) - 1, -1, -1):  #iterating in reverse order : can do in regular order as well
            nextDP = set()  #since cannot update dp set while iterating it
            for t in dp:    #for every total in dp set
                if (t + nums[i]) == target:
                    return True  #return true only if target is in dp else return false 
                nextDP.add(t + nums[i])
                nextDP.add(t)  #do not want to lose all original values in dp
            dp = nextDP
        return False

print(canPartition([1,5,11,5]))
print(canPartition([1,2,3,5]))
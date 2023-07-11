"""
https://leetcode.com/problems/jump-game/
https://www.youtube.com/watch?v=Yan0cv2cLy8&list=PLot-Xpze53lfOdF3KwpMSFEyfE77zIwiP&index=25

leetcode 55
medium
greedy

input : integer array nums
initially positioned at the array's first index, and each element in the array represents
your maximum jump length at that position.
output: Return true if you can reach the last index, or false otherwise.

Logic : 
-approach1 : brute force O(n^n) 
-from 1st node : x branches where x = val of 1st ele
-then from each branch : y branches where y = val of 2nd ele
and so on recursively

-if all leafs = dead ends != last index -> return false 

-approach2 : -> O(n^2) with caching but needs extra memory 
eg : [3,2,1,0,4]
index 0,1,2,3,4
at index 2 to index 3 to index 4: deadend -> cannot reach last index from index 2
-> dp[3] = False
-> dp[2] = False
-so not needed to go down the dp[2] path again in another branch since
we know that dp[2] = False
-so in another branch dp[1] also = False
-and dp[0] = false -> return false 

-approach 3: greedy : O(n)
-simple solution
-look at reverse order
-start from last index, and go to beginning 
eg : [2,3,1,1,4]
index 0,1,2,3,4
so from index 3 -> index 4 possible
so change target to index 3
so can index 2 reach index 3 (index2 doesnt need to reach index 4)
recursively keep shifting target to left
-possible from 1st position as well -> return true 
Time Complexity: O(n) and space : o(1) : no extra memory/decision tree/ cache 

"""

def canJump(nums):
        goal = len(nums) - 1  #the only var needed extra 

        for i in range(len(nums) - 2, -1, -1): #loop from back to 1st index 
            #nums[i] : jump length 
            # so starting at index/position i : with a jumo length nums[i], can we reach target 
            if i + nums[i] >= goal:  
                goal = i  #if yes, then shift target 1 left 
        return goal == 0  #in the end, if goal = 0, we reached the beginning -> return true 


print(canJump([2,3,1,1,4]))
print(canJump([3,2,1,0,4]))
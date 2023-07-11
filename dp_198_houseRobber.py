"""
https://leetcode.com/problems/house-robber/

leetcode 198
medium

dynamic prg

input : nteger array nums representing the amount of money of each house
output: maximum amount of money you can rob tonight without alerting the police.

constraint : adjacent houses have security systems connected and it will 
automatically contact the police if two adjacent houses were broken into on the same night.

Logic : 
approach 1 : brute force 
for eg : [1, 2, 3, 1] 
-1 ele : 1 
-1 skip 2
-now from node 1 : 2 paths 3 or 1
- go with path with max sum
- rob house 2 : other decision

approach 2: dp 
begin with 1 ele : leave out the neighbrors, check max from rest(again tree : select or not select each ele) : 1 ele + max from rest 
(=subproblem : repeat work) = sum : check if this sum is max out of all iterations similarly 

recurrence relation : rob = max(arr[0] + rob[2:n], rob[1:n])
i.e max(@@1, @@2)
where @@1 : decision to rob 1st house + first sub problem=recurring relation on rob of 2nd to last, skipping index 1
@@2 : or we decide not to rob first house : rob[1:n]

so entire result depends on arr[0] and rob[1:n] only 
Time Complexity: O(n)

"""

def rob(nums):
        # we only need to maintain max of the last 2 houses robbed from
        # so only 2 variables
        # initialize as 0 because if we get an empty subarray we will return 0 itself

        rob1, rob2 = 0, 0

        # iterate thru each house
        for n in nums:
            # [rob1, rob2, n, n+1...]
            # rob2 = last house robbed
            # rob1 = house before that 
            # compute max value that can be robbed till house n = n + rob1
            temp = max(n + rob1, rob2)

            # update rob1 to rob2 and rob2 to n so to temp for now
            rob1 = rob2
            rob2 = temp

        # this will be the last value : max from entire neighborhood 
        return rob2

print(rob([1,2,3,1]))
print(rob([2,7,9,3,1]))
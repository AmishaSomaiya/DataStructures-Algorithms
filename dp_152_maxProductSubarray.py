"""
https://leetcode.com/problems/maximum-product-subarray/

leetcode 152
medium
dp

input : integer array nums
output: find a subarray that has the largest product, and return the product.

Logic : 
approach 1 : brute force
-find subarray starting from each position, find prod for each subarray, see if its max, update prod result

patterns :
1. if all positive ints in subarray :
-product will keep increasing
2. if all negative ints :
-when odd number of elements with continuous negative eles, final prod will be negative so prod gets smaller
-and in the middle somewhere the prod will be bigger when (-)(-)=(+)
-eg : (-1,-2,-3) then -1.-2.-3 = -6 but -2.-3 = prod of substring = 6 > -6 

so approach 2:
-find prod of subarray of first 2 eles first then use that to find prod of 1 more ele added to the prod
- so if prod of subarray is neg, then if new ele is pos, then this prod with new ele will be smaller to prev prod
- so we want to get max(prod ofprev, prod with new ele add)
- we also want to get min(prod from prev subarray ) = min(-1, -2)=-2
- so find max prod and min prod at every iteration of loop
-1 edge case remains : ele value = 0 both max and min prod becomes 0,
so whenever ele=0, reset max and min to 1 i.e. ignore 0s 
Time Complexity: O(n), space : O(1)

"""
def maxProduct(nums):
        
        res = nums[0]  #and not to 0
        curMin, curMax = 1, 1 #and not to 0

        for n in nums:  #loop thru each ele in nums
            if n==0:    #ele=0 edge case 
                  curMin, curMax = 1,1
                  continue
            # else : 
            tmp = curMax * n
            curMax = max(n * curMax, n * curMin, n)  #if n and curMin are both neg, then n.curMin will be max 
            curMin = min(tmp, n * curMin, n)  #if tmp is not used, curMax will be used again : wrong, since we want prev curMax and not recomputed curMax 
            res = max(res, curMax)
        return res

print(maxProduct([2,3,-2,4]))
print(maxProduct([-2,0,-1]))

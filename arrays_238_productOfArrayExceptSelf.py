'''
https://leetcode.com/problems/product-of-array-except-self/
https://www.youtube.com/watch?v=bNvIQI2wAjk&list=PLot-Xpze53lfOdF3KwpMSFEyfE77zIwiP&index=33

leetcode 
medium
arrays

input : an integer array nums
output: array of products except self


Explanation: Since we only iterate nums twice and all of operations inside loops are 
performed in constant time, so the algorithm runs in O(2*n) = O(n) time. 
Suppose nums = [a, b, c, d]. After first loop, we will get output_list = [1, a, ab, abc]. 
Noted that the value of the last element is exactly the product of array except self. 
With this in mind, we only need to iterate nums backward to calculate the value of each 
element via suffix_poduct. In the second for-loop, when i = len(nums)-1 (the last element), 
output_list[i] is exactly output_list and suffix_product = 1 * d. When i=len(nums)-2, 
the value will be output_list[i] * suffix_product = ab * d = abd. As as result, we get an 
array with its value is the product of array except self.

constraints : 1.in O(n) 2.without using division operator 

approach 1 : T:O(n) but S:O(n)
-get product of every value before that ele and product of every value after that ele
and multiply both : O(n) time 
-prefix of 1st ele and postfix of last ele = take as 1 

approach 2 : T:O(n) S:O(1)
-store prefix and post fix in output array directly, so avoid extra memory
-so 2 passes on nums : 
-after 1st pass : prefix for ele at index 3 stored at index 3 of output
=after 2nd pass : postfix for ele at index 3 * by prefix already at index 3 of output
and now prefix replaced by prod of pre and postfix at index 3 of output 

'''

from typing import List


def productExceptSelf(nums: List[int]) -> List[int]:
        res = [1] * (len(nums))  #not counted as extra memory in context of this problem 

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res


print(productExceptSelf([1,2,3,4]))
print(productExceptSelf([-1,1,0,-3,3]))
print(productExceptSelf([0,0])) 
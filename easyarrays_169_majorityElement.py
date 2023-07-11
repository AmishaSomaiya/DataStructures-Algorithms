"""
https://leetcode.com/problems/minimum-height-trees/

leetcode 169
easy
arrays, hash table 

input : array nums of size n
output: the majority element

assume that the majority element always exists in the array.

brute force approach :
def majorityElement(nums: List[int]) -> int:
    for i in range(len(nums)):
        counter = sum(1 for number in nums if number == nums[i])
        if counter > len(nums) // 2:
            return nums[i]
Time Complexity: O(n^2), Space Complexity: O(1)

improved : hash table 
Time Complexity: O(n), Space Complexity: O(n)

"""

def majorityElement(nums):
        count = 0
        length = len(nums)
        newdict = {}
        
        # if there is single element, then that itself is the majority element
        if length == 1:
            return nums[0]

        # loop on nums 
        for i in nums:
            # if ele already present, incre its count and if count > length/2
            # else add ele to dict
            if i in newdict:
                count = newdict.get(i)
                newdict[i] = count+1
                count +=1
                if count > length/2:
                    return i
            else:
                newdict[i] = 1


print(majorityElement([3,2,3]))
print(majorityElement([2,2,1,1,1,2,2]))
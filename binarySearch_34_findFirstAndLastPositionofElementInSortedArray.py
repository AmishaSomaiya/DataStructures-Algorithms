"""
https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
https://www.youtube.com/watch?v=4sQL7R5ySUU&list=PLot-Xpze53lfOdF3KwpMSFEyfE77zIwiP&index=63

leetcode 34
medium
binary search 

input : int array sorted in asc order
output: find starting and end pos of given target value
return [-1, -1] if target not found in array 

Logic : 
approach 1 : o(n)
linear search and return 1st and last index of target value : o(n)

approach 2 : o(logn)
binary search
left and right pointer, compute middle value,
if middle<target, look into right portion of array
i.e. update left = middle+1, right as it is
recompute middle
now we want the leftmost and rightmost target values 
modify binary search algo
to look for rightnost target : keep looking
shift left pointer to middle + 1 of recent search portion
when left=right pointer and no more values to the right of it and right most value = target
then this = rightmost target value

for leftmost target value :
restart binary search 
init pointers again , compute mid, update pointers, recompute mid
now to find leftmost value, now left as it is, right = mid - 1

Time Complexity: o(logn) twice = still o(logn)

"""

from typing import List


def searchRange(nums: List[int], target: int) -> List[int]:
        left = binSearch(nums, target, True)  #looking for leftmost value 
        right = binSearch(nums, target, False)  #rightmost value 
        return [left, right]

    # leftBias=[True/False], if false, res is rightBiased
# helper func since need to do this twice
# third arg = leftbias = true/false
# true : means looking for leftmost index
# false : means looking for rightmost index
def binSearch(nums, target, leftBias):
        l, r = 0, len(nums) - 1 #initialize pointers 
        i = -1  #var when target found 
        while l <= r:  #iterate till left != right 
            m = (l + r) // 2 #compute mid, integer division 
            if target > nums[m]:  #as explained above, search towards right 
                l = m + 1
            elif target < nums[m]: #search to the left 
                r = m - 1
            else:
                i = m #target found, regular bin search till here 
                if leftBias:  #looking for leftmost target value 
                    r = m - 1
                else:
                    l = m + 1 #looking for rightmost target value 
        return i  #return -1 if target not found 


print(searchRange([5,7,7,8,8,10],8))
print(searchRange([5,7,7,8,8,10],6))
print(searchRange([],0))



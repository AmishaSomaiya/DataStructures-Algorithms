"""
https://leetcode.com/problems/kth-largest-element-in-an-array/
https://www.youtube.com/watch?v=XEmy13g1Qxc&list=PLot-Xpze53lfOdF3KwpMSFEyfE77zIwiP&index=61

leetcode 215
medium
quick select 

input : an integer array nums and an integer k
output: return the kth largest element in the array.
Note that it is the kth largest element in the sorted order, not the kth distinct element.
Can you solve it without sorting?  

Logic : 
-largest in sorted array not distinct so array can have duplicates

approach 1 : 
-sort : o(nlogn) and then return the kth largest 
i.e. index length-k

approach 2 : best for worst case : heap 
use max heap
-heapify (turn into a heap) in o(n) time
-pop k times o(logn) time once -> klogn
so better than sorting : o(n + klogn)

approach 3 : o(n) for avg case [o(n^2) in worst case]
-select pivot
-from beginning of array : compare each ele with pivot, 
-place ele in left half or right half
-in-place
-partition the array, partitions not in sorted order
-so partition1(everything <pivot), pivot, partition2
-so we know target value is in partition2 
-quick sort the partition2 : so time : n + n/2 + n/4 + ... = o(2n) = o(n) instead of o(nlogn) for avg case
return kth largest ele




Time Complexity: 

"""

# Solution: Sorting
# Time Complexity:
#   - Best Case: O(n)
#   - Average Case: O(n*log(n))
#   - Worst Case:O(n*log(n))
# Extra Space Complexity: O(n)


from typing import List


class Solution1:  #sorting solution 
    def findKthLargest(nums: List[int], k: int) -> int:
        nums.sort()
        return nums[len(nums) - k]


# Solution: QuickSelect
# Time Complexity:
#   - Best Case: O(n)
#   - Average Case: O(n)
#   - Worst Case: O(n^2)
# Extra Space Complexity: O(1)

# recursive quick select 
# left, right : pointers that decide the portion of the array on which quick select to apply
def partition(nums: List[int], left: int, right: int) -> int:
        pivot, fill = nums[right], left #pivot : right most value since easy, and fill pointer at left most value 

        for i in range(left, right):  
            if nums[i] <= pivot:  #swap with fill index ele if <=
                nums[fill], nums[i] = nums[i], nums[fill]  #swap in python 
                fill += 1

        nums[fill], nums[right] = nums[right], nums[fill]  #swap fill index value with pivot value 

        return fill

def findKthLargest(nums: List[int], k: int) -> int:
        k = len(nums) - k
        left, right = 0, len(nums) - 1

        while left < right:
            pivot = partition(nums, left, right)

            if pivot < k:   #if k > p then look into right portion of array, so change left pointer, right pointer remains same 
                left = pivot + 1
            elif pivot > k:  #i.e. k < p then run quick select on left portion of the array  
                # left pointer remains the same, right gets shifted 
                right = pivot - 1
            else:  #if p exactly = k then p is the kth largest ele, return it 
                break

        return nums[k]
    
print (findKthLargest([3,2,1,5,6,4], 2))
print (findKthLargest([3,2,3,1,2,4,5,5,6], 4))
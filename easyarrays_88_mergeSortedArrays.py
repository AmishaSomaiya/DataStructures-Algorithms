"""
https://leetcode.com/problems/merge-sorted-array/
https://www.youtube.com/watch?v=P1Ic85RarKY&list=PLot-Xpze53lfQmTEztbgdp8ALEoydvnRQ&index=8

leetcode 88
easy

input : two integer arrays nums1 and nums2, sorted in non-decreasing order, 
and two integers m and n, representing the number of elements in nums1 and nums2 respectively.  
output: Merge nums1 and nums2 into a single array sorted in non-decreasing order.

Logic : 
-cant use extra space
-start merging from behind since we know extra space in the end provided
-so 1 pointer at the end
-compare last filled value in nums1 and nums2
-whichevr is bigger put it in last position of nums1 where there is empty space
-decrement pointer of that nums1 or nums2 by 1
-m and n are index of last values in nums1 and nums2



Time Complexity: O(n), space complexity : O(1)

"""
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        while m>0 and n>0 : #there are elements in both
            if nums1[m-1] >= nums2[n-1] :
                nums1[m+n-1] = nums1[m-1]
                m-=1
            else : 
                nums1[m+n-1] = nums2[n-1]
                n-=1
        
        # if still elements left in nums1: do nothing since they are already sorted and in the 
        # beginning
        # but if elements left in nums2 :
        if n>0 :
            nums1[:n] = nums2[:n]

        # no return,inplace

    
merge([1,2,3,0,0,0], 3, [2,5,6], 3)
merge([1], 1, [], 0)





"""
https://leetcode.com/problems/container-with-most-water/

leetcode 11
medium
arrays 

input : an integer array height of length n
output: the maximum amount of water a container can store

Logic : two pointers 
Sorting intervals can make sure that for any 0 <= i <= size of intervals-1, 
intervals[i][0]<=intervals[i+1][0], 
which is a great property that we only need to change end time in overlapping cases.

pseudo-code : 
use 2 pointer method
initialize left and right pointers  
loop till left != right :
       # if height[left] is smaller, the only way to increase volume is to check whether
        # moving left to left + 1 increase the volume since width is getting smaller.
return max volume
Time Complexity: O(n), Space Complexity: O(1)

"""

from typing import List

def maxArea(height):
    maxVolume = 0
    left = 0
    right = len(height)-1

    while left != right :
        if height[left] >= height[right]:
            volume = height[right]*(right-left)
            right -=1
        else :
            volume = height[left]*(right-left)
            left +=1

        maxVolume = max(maxVolume, volume)
    return maxVolume

print(maxArea([1,1]))
print(maxArea([1,8,6,2,5,4,8,3,7]))

            

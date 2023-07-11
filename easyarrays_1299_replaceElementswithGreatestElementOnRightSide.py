"""
https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/
https://www.youtube.com/watch?v=ZHjKhUjcsaU&list=PLot-Xpze53lfQmTEztbgdp8ALEoydvnRQ&index=15

leetcode 1299
easy

input : an array arr
output: replace every element in that array with the greatest element among the elements to its right, and replace the last element with -1.
After doing so, return the array.

Logic : 


Time Complexity: 

"""

from typing import List


def replaceElements(arr: List[int]) -> List[int]:
        rightMax = -1
        for i in range(len(arr) -1, -1, -1):
            newMax = max(rightMax, arr[i])
            arr[i] = rightMax
            rightMax = newMax
        return arr

print(replaceElements([17,18,5,4,6,1]))
print(replaceElements([400]))
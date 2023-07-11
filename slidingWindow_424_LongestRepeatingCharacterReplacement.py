"""
https://leetcode.com/problems/longest-repeating-character-replacement/
https://www.youtube.com/watch?v=gqXU1UyA8pk&list=PLot-Xpze53lfOdF3KwpMSFEyfE77zIwiP&index=29

leetcode 424
medium
sliding window 

input : a string s and an integer k
output: choose any character of the string and change it to any other uppercase English character. 
You can perform this operation at most k times.
Return the length of the longest substring containing the same letter you can get after performing the above operations.

Logic : 
approach : brute force :O(n^2) with sliding window 
check each substring 
we are performing replacement of least freq char to match the rest of most freq chars 
maintain hashmap of char and count of char 
1. to check if substring is valid -> windowlen - count(most freq char)
= number of characters to be replaced in the window to match the most freq char 
if it is <= k then valid 
2. which is the most freq char in the window 
from hashmap 
size of hashmap is max 26 since 26 capital letters 
so finding the most freq char = O(26) = ineff but still linear time 
3. sliding window 
start at the beginning position (left), expand the window to the right, 
keep expanding to the right till condition satisfied.
when condition no longer satisfied, shift the left pointer by 1 position and
again start expanding the window 
repeat recursively
-initially both left and right at the beginning 
-result = length of longest valid window
Time Complexity: O(26.n) = O(n)

"""


def characterReplacement(s: str, k: int) -> int:
        count = {}  #hashmap to count occurrences of each char 
        res = 0     #var to hold length of longest substring with k replacements 

        l = 0   #left pointer which will begin at index 0
        maxf = 0 #maxf pointer which will iterat thru the array 
        for r in range(len(s)): #for the char at position r 
            count[s[r]] = 1 + count.get(s[r], 0)  #increment count of char
            maxf = max(maxf, count[s[r]]) #second term: freq of char just added : O(1) operation 

            # ensure the current window is valid 
            # if not valid : then incre left counter and decre count of char 
            if (r - l + 1) - maxf > k:
                count[s[l]] -= 1
                l += 1 #incre left pointer 

            res = max(res, r - l + 1) #update result with max length = max size of the window = r-l+1 
        return res

print(characterReplacement("ABAB",2))
print(characterReplacement("AABABBA",1))
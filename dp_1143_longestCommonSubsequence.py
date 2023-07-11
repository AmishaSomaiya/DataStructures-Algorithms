"""
https://leetcode.com/problems/longest-common-subsequence/
https://www.youtube.com/watch?v=Ua0GhsJSlWM&list=PLot-Xpze53lfOdF3KwpMSFEyfE77zIwiP&index=21

leetcode 1143
medium
dynamic programming brute force bottomup 

input : two strings text1 and text2
output: return the length of their longest common subsequence. 
If there is no common subsequence, return 0.

A common subsequence of two strings is a subsequence that is common to both strings.

Logic : 
-start from 1st char in each string, incre pointer in that string, new position : new subproblem : dp
-break into subproblems based on particular char is equal or not equal 
-2d grid along 1 dimension : 1 string, another dimension : another string 
-then will begin at the bottom-rightmost, solve subprobs and move towards topleft most 
-if first char of subseq matches then go diag so we can check remainder of seq
-if char1 == char2 : go diagonally down -> 1+diag
             else  : go right or down   -> max(right,down)
-once complete reached bottom rightmost : go back on the path to the topright most = answer 
-edge case : out of bounds : give default value of 0 to the row and column to the right and bottom out of bound case 
Time Complexity: O(n.m) i.e product of lengths of strings 
space complexity = same because that much memory needed for dp table/2d grid 

"""

def longestCommonSubsequence(text1, text2):
        # initialize 2d grid of size (len2+1).(len1+1)
        dp = [[0 for j in range(len(text2) + 1)] for i in range(len(text1) + 1)] #list comprehension, +1 because to put all 0s for out of bounds 

        for i in range(len(text1) - 1, -1, -1):
            for j in range(len(text2) - 1, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]  #1+diag: 1 added because chars matched so add 1
                else:  #else chars dont match so do not add 1 now 
                    dp[i][j] = max(dp[i][j + 1], dp[i + 1][j])

        return dp[0][0]

print(longestCommonSubsequence("abcde","ace"))
print(longestCommonSubsequence("abc","abc"))
print(longestCommonSubsequence("abc","def"))
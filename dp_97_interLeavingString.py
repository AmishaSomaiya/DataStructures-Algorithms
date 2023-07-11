"""
https://leetcode.com/problems/interleaving-string/
https://www.youtube.com/watch?v=3Rw3p9LrgvE&list=PLot-Xpze53lfOdF3KwpMSFEyfE77zIwiP&index=53

leetcode 97
medium
dp

input : 
output: 

Logic : 
-allowed to split strings in any way(length of substrings can be anything)
but splitting and interleaving 1 and 2 should result in str 3

approach : dp, 3 pointers 
-compare 1st chars from both strings and see which one matches the 1st string of 3rd string :
so begin with that : continue on that string till matches with str3 chars : 
move pointer to the starting position after the matched substring : new sub prob 

-edge cases :
1. if a char encountered : not in str 1 or str 2 as per sequence : then not possible to interleave 1 and 2 to make str 3
2. if char from str 3 matches both curr char from str 1 and str 2 
: solun : 1. backtracking
          2. caching (to avoid repeated work) + dp 
          3. only dp


approach 1 : brute force 
decision tree :
i1, i2, i3 : pointer for str1, str2, str3
i3=i1+i2
worst case: 2 decisions from each branch : o(2^(n+m))

dp + caching approach : 
since repeated work avoided by caching 
Time Complexity: O(mn)
(pointer1, pointer2) : m possible positions for 1st, n possible positions for 2nd :
so o(m.n) 

dp approach :
-when both strs out of bounds : end : base case
-1 extra row and col
-table out of bounds for bottom right cell : base case
and backtracking
and also need to count for out of bounds position

--
can also work out the dp recursive soln

"""


def isInterleave(s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):  #if they dont add up to i3, then return false straight 
            return False

        # else init 2dim array dp with dims len1*len2+1 because we also need to check out of bounds 
        dp = [[False] * (len(s2) + 1) for i in range(len(s1) + 1)]
        dp[len(s1)][len(s2)] = True  #bottom-rightmost cell 

        for i in range(len(s1), -1, -1):
            for j in range(len(s2), -1, -1):
                # if i is still in bounds AND does that char equal the target char we r looking for 
                # AND 3rd !=dfs we dont want to compute dfs rather check if dp[next char] is true 
                # because backtracking so next char soln already should be found 
                if i < len(s1) and s1[i] == s3[i + j] and dp[i + 1][j]:
                    dp[i][j] = True #so then dp[i][j] should be set to true 
                if j < len(s2) and s2[j] == s3[i + j] and dp[i][j + 1]: #similarly for str2
                    dp[i][j] = True
                # if both are false, then dp[i][j] = false but already init to false 
        return dp[0][0]

print(isInterleave("aabcc","dbbca","aadbbcbcac"))
print(isInterleave("aabcc","dbbca","aadbbbaccc"))
print(isInterleave("","",""))

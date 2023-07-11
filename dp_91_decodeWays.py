"""
https://leetcode.com/problems/decode-ways/
https://www.youtube.com/watch?v=6aEyTjOwlJU&list=PLot-Xpze53lfOdF3KwpMSFEyfE77zIwiP&index=39

leetcode 91
medium
dp

input : a string s containing only digits,
output: return the number of ways to decode it.

Logic : 
aapproach1 : brute force O(2^n)
1-9 will have sigle mapping but from double digits eg 10->
1,0 can be mapped separately or as 10 so leading to decision tree 
-any nymber except 0 can be repeated after itself as 1 of the branches in the decision tree 
but edge cases
so either can consider 1 digit or if considering 2 digit : that digit <= 26
as per mapping given in question
so if 2 digit then 1st digit should be 1 or 2 i.e. >2 ; 1st digit compulsory < = 2
Time Complexity: O(2^n) since 2 decisions (1 or 2) at every input string so not eff

approach2 : with cache O(n), s:O(n)
subprob : in how many ways subportion of the string can be decoded 
use index i
and cache of size n to store #ways for each index 
then to find #ways for 2 decisions = O(1) operation since no looping anymore

approach3 : dp without cache :


"""
def numDecodings(s: str) -> int:
        # Memoization
        dp = {len(s): 1} #hashmap or cache : init to single value 1, so return 1 in case of empty string : good base case 
        def dfs(i): #recursive funct with index i : curr position in string s
            if i in dp:  #another base case : if i in dp i.e. i already cached or i = the last position in the string  
                return dp[i]  #good base case 
            # else if not end of string, check the curr char at i : 
            if s[i] == "0":  #bad base case , starting with 0: invalid : return 0 
                return 0  #cannot decode string starting at 0 so return 0 

            # else if not 0 then it is between 1 and 9 : so it becomes a single digit subproblem 
            res = dfs(i + 1) #then recursive call to dfs with parameter i+1 
            #sometimes can call i+2 instead of only i+1 : double digit 
            # 1st condition in if : if 1 more digit exists after ith position 
            # AND either char i+1 starts with 1 or 2 but < 26 i.e. between 10 to 26 
            if i + 1 < len(s) and (  
                s[i] == "1" or s[i] == "2" and s[i + 1] in "0123456"
            ):  #if condition satisfied then add to result 
                res += dfs(i + 2)
            dp[i] = res  #cache the result and return it to outer func
            return res

        return dfs(0)  #call dfs recursively starting from index 0 

        # Dynamic Programming
        dp = {len(s): 1}
        for i in range(len(s) - 1, -1, -1):
            if s[i] == "0":
                dp[i] = 0
            else:
                dp[i] = dp[i + 1]

            if i + 1 < len(s) and (
                s[i] == "1" or s[i] == "2" and s[i + 1] in "0123456"
            ):
                dp[i] += dp[i + 2]  #here this is added, above we called this recursively 
        return dp[0]

print(numDecodings("12"))
print(numDecodings("226"))
print(numDecodings("06"))



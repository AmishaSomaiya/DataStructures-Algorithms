"""
https://leetcode.com/problems/word-break/

leetcode 139
medium

input :  a string s and a dictionary of strings wordDict
output: return true if s can be segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

Logic : decision tree -> caching -> dp
-from the first ele, keep appending 1 char to it at a time, 
till it is found in the dict then begin fresh with the next element
= subprob starting from a new position
-for size n, we will try all the words in the word dict
=> max sie of word dict < max size of the string = O(n.m) and then .n because we are checking each word in the dict , 
so efficient : O(n.m.n)
approach : bottom-up approach 
-check the first word in the word dict : 4 chars long 
so match with the first 4 chars in the string 
-if match found, then proceed to the next word in the word dict
and the next char in the string and repeat : subprob 


cache approach :
-keep track of index and change of index once a word is found from the dict
so single variable index will be tracked in the backtracking solution 
-number of decisions = number of words in the word dict

for eg : s="greatsun"
and word dict = ["great", "son", "sun"]

so each word from the word dict is matched with the corresponding number of chars in the string s
so in the decision tree : index i=0 -> great, son, sun
so when son is matched with substring in s of size 3 : son is not found
so this path is closed, no need to go further on this path in the decision tree
similarly, tha path from "sun" is also closed because it doesnot match the first 3 chars in s

similarly, great is compared and match is found.
so 3 more decisions (since 3 words in the dict) from the node great 
to the next level in the decision tree. since match is found, 
index is incre to +5. 

process repeated till index = right after end of string  -> return true 

approach : cache 
base case : dp[8] = true since it is length of the string, so if this position is reached,
it is true 
now bottom up approach : go thru every single index in reverse order :
for s = "neetcode", worddict " "neet", code", "leet"
now dp[7] = false because dp[7] = just last char = n and not != len (any word in word dict )
similarly, dp[6] = false
           dp[5] = false
but,       dp[4] = true 
           dp[3] = dp[2] = dp[1] = false because cannot word break the string if we start at any of these positions
           dp[0] = dp[0+4] = true 
                 = starting at index 0, match is found, so after this directly go 
           to the index after the matched word and find from dp table above 
Time Complexity: O(n.m.n)

"""
def wordBreak(s, wordDict):
        dp = [False] * (len(s) + 1)  #cache : 1d array initialized as false, +1 for the base case 
        dp[len(s)] = True #base case dp[8] in the eg above 

        for i in range(len(s) - 1, -1, -1):  #loop from last index to beginning 
            for w in wordDict:  #for each position i, we want to try each word from the word dict
                if (i + len(w)) <= len(s) and s[i : i + len(w)] == w:  #first part : confirm if there are enough chars in s to compare with w
                # second part in the if condition above : s[from i] match with w 
                    dp[i] = dp[i + len(w)]  #index incre by len(w) if match found 
                if dp[i]:  #if word match found at this index, wordbreak it and proceed to next index, repeat till index 0
                    break

        return dp[0]  #since began from backward 

print(wordBreak("leetcode", ["leet","code"]))
print(wordBreak("applepenapple", ["apple","pen"]))
print(wordBreak("catsandog", ["cats","dog","sand","and","cat"]))
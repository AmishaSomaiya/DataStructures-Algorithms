"""
https://leetcode.com/problems/palindrome-partitioning/
https://www.youtube.com/watch?v=3jvWodd7ht0&list=PLot-Xpze53lfOdF3KwpMSFEyfE77zIwiP&index=28

leetcode 131
medium
backtracking

input : string s
output: partition s such that every substring of the partition is a palindrome. 
Return all possible palindrome partitioning of s.

Logic : O(2^n)
approach : bruteforce backtracking 
-1st partition : each char by itself 
-partition, check if palindrome, add to result if yes
-decision tree :
-number of branches = length of string 
-1st branch : single char 
-2nd branch : 1st 2 chars
-3rd branch : 1st 3 chars
-at every node : check if pali
-if not, stop that branch
-also stop if leaf node reached and pali : add to result 


Time Complexity: O(2^n)

"""
def partition(s):
        res, part = [], [] #result to store all partitions, part = current partition 

        def dfs(i): #i : index of current char, recursive func
            if i >= len(s): #if out of bounds, index >= length of string : 
                res.append(part.copy()) #since partition var will be overwritten in another branch
                return #base case 
            for j in range(i, len(s)):  #iterate thru each char till end of string reached 
                if isPali(s, i, j):  #check if this substring is a pali or not
                    part.append(s[i : j + 1]) #if yes, then add this substring to current partition
                    dfs(j + 1)  #j+1: next char, so recursively perform dfs to find additional pali
                    part.pop() #cleanup current partition for next iteration

        dfs(0)  #call dfs with start index = 0
        return res #return result 

def isPali(s, l, r):  #parameters : string, left and right boundary
        while l < r:
            if s[l] != s[r]:
                return False
            l, r = l + 1, r - 1
        return True


print(partition("aab"))
print(partition("a"))
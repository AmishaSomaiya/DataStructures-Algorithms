"""
https://leetcode.com/problems/word-search/
https://www.youtube.com/watch?v=pfiQ_PS1g8E
https://neetcode.io/practice

leetcode 79
medium
graphs

Logic : DFS, recursive backtracking

input : m x n grid of characters board and a string word
output: true if word exists in the grid.

explanation:
start from the first letter in the word : check if it is in any cell, if yes, check the next letter
in the word, if it is in any of the neighbors of this cell...such that cant reuse

pseudocode:
-declare dims of the board
-since 1 cell cannot be visited again in current path, make a set() path for all cells currently
in the path, so the same position is not visited twice in the path
-create nested dfs func within the actual function : so board and word need not be passed
but row, col, current char:i we are looking in the target word : these 3 need to be passed
-now in this dfs function : if end of word reached, i..e i = last position:
good case, return true
-if out of bounds, or wrong char found -> return false
-if current position is in the path set : i.e. visiting the same position
twice -> return false
-if none of these, char found -> continue with DFS with another char
-run DFs on all 4 neighboring adjacent positions -> if any of them return true 
answer is true

-now only thing left is brute force : run above dfs func for every single position on 
the board
if dfs returns true, return true 


Time Complexity: O(nm4^w), Space Complexity: O(nm), 
where n is the number of row, m is the number of column, and w is the length of word.

n*m = size of board 
O(n*m*dfs)*4^w -> O(n*m*4^w)
"""
from collections import Counter, defaultdict

def exist(board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        ROWS, COLS = len(board), len(board[0])
        path = set()

        def dfs(r, c, i):
            if i == len(word):
                return True
            if (
                min(r, c) < 0
                or r >= ROWS
                or c >= COLS
                or word[i] != board[r][c]
                or (r, c) in path
            ):
                return False
            path.add((r, c))
            res = (
                dfs(r + 1, c, i + 1)
                or dfs(r - 1, c, i + 1)
                or dfs(r, c + 1, i + 1)
                or dfs(r, c - 1, i + 1)
            )
            path.remove((r, c))
            return res

        # To prevent TLE,reverse the word if frequency of the first letter is more than the last letter's
        count = defaultdict(int, sum(map(Counter, board), Counter()))
        if count[word[0]] > count[word[-1]]:
            word = word[::-1]
            
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True
        return False

print(exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED"))
print(exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "SEE"))
print(exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCB"))
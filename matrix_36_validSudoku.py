"""
https://leetcode.com/problems/valid-sudoku/
https://www.youtube.com/watch?v=TjFXEUCMqI8&list=PLot-Xpze53lfOdF3KwpMSFEyfE77zIwiP&index=49

leetcode 36
medium

input, output:
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:
A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
 
Logic : 
-for this problem, we have to determine valid or not based on filled cells 
and not by assuming anything in unfilled cells : so easier 

1. every row does not have duplicates : use hashset
-hashset for every row
2. similarly hashsets for cols
Time Complexity: till now : size of grid : o(n^2)
3. hashset for 3x3 grids 

overall : time : o(n^2) : loop thru overall grid
space : o(n^2) for hashset

approach : 
row and col along dims 
but how to know which index in which 3x3 subgrid :
so give subgrid numbers along row and col dim
then index number 4,4 -> convert to subgrid number say 1,1
index numbers 0-9 -> subgrid numbers 0-2 by integer div : index/3
edge cases : 8/3 = 2, 2/3 = 0 works

hashset : key : converted row, col pair = row/3, col/3
value : hashset 

"""

from collections import defaultdict
from typing import List


def isValidSudoku(board: List[List[str]]) -> bool:
        cols = defaultdict(set)  #hashmap : key, value : conv row, col pair, hashset 
        rows = defaultdict(set)
        squares = defaultdict(set)  # key = (r /3, c /3)

        for r in range(9):  #loop thru entire grid 
            for c in range(9):
                if board[r][c] == ".":  #if empty, skip it 
                    continue
                # else check for duplicates 
                if (
                    board[r][c] in rows[r]  #rows:hashset, r: current row so rows[r] represents hashset of all values that occur in this row number r
                    or board[r][c] in cols[c] #so if board[r][c] in rows[r] or cols[c], then it is a duplicate 
                    or board[r][c] in squares[(r // 3, c // 3)] #or in current subgrid 
                ):  #if it is a duplicate : return false 
                    return False
                cols[c].add(board[r][c])  #else if valid, then continue and add this to all 3 sets 
                rows[r].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])

        return True  #if no dups detected in entire grid 

print(isValidSudoku([["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]))




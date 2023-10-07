"""
https://leetcode.com/problems/combination-sum/

leetcode 682
easy
stack

input : a list of strings operations, where operations[i] is the ith operation you must apply to the record and is one of the following:

An integer x.
Record a new score of x.
'+'.
Record a new score that is the sum of the previous two scores.
'D'.
Record a new score that is the double of the previous score.
'C'.
Invalidate the previous score, removing it from the record.
output: Return the sum of all the scores on the record after applying all the operations.

Logic : use stack to add and remove elements in o(1) time, keep track of elements to add to the sum


Time Complexity: o(n)
space : o(n) for the stack 

"""

class Solution:
    def calPoints(self, operations) -> int:
        stack = []
        for i in operations :
            if i=="+":
                stack.append(stack[-1]+stack[-2])
            elif i=="D":
                stack.append(stack[-1]*2)
            elif i=="C":
                stack.pop()
            else :
                stack.append(int(i))
        return sum(stack)

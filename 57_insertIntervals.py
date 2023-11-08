"""
https://leetcode.com/problems/insert-interval/
https://www.youtube.com/watch?v=A8NUOmlwOlM&list=PLot-Xpze53lfOdF3KwpMSFEyfE77zIwiP&index=68

leetcode 57
medium

input : given an array of non-overlapping intervals where intervals[i] = [starti, endi] represent
the start and the end of the ith interval and intervals is sorted in ascending order by starti. 
You are also given an interval newInterval = [start, end] that represents the start and end of another 
interval.

output: Insert newInterval into intervals such that intervals is still sorted in ascending order by 
starti and 
intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).
Return intervals after the insertion.

Logic : 
approach : 
if intervals overlap: merge them : 
take min of both of them and set as interval start and
take max of both of them and set as interval end 

if not overlapping : keep them as it is 

already sorted based on start time 
overlap on single point considered as overlap

case 1 : simple case
if the int to be inserted doesnt overlap with the 1st int, it cannot overlap with 
any other int going forward because ints are sorted
so just insert new int at beginning and append orig list after that 
and return it

case 2 : simple case
similarly if start value > end value of last int

case 3 :
new int overlaps with multiple ints: then will need to merge with all of them 

case 4 :
new int between 2 ints and doesnt overlap with any int, just insert without merge 

how do we check if overlap :
if not (new end value < int start 
AND
if new start value > int end )
i.e. if new doesnt go before or after this int :
=> overlapping 

if overlapping then how to merge :
take min of starts and max of ends 

do not add to output just yet because this could overlap with other ints in list

end val of curr < start value of new so not overlapping
then add both to the result 
repeat till ints remaining 


Time Complexity: since already sorted so only go thru once
so o(n): linear and space : o(n) for result array 


 res = []
 for i in range(len(intervals)):
         if newInterval[1] < intervals[i][0]:
                 res.append(newInterval)
                 return res + intervals[i:]
         elif newInterval[0] > intervals[i][1]:
                 res.append(intervals[i])
         else:
              newInterval = [
                    min(newInterval[0], intervals[i][0]),
                    max(newInterval[1], intervals[i][1]),
                ]
        res.append(newInterval)
        return res

"""

from typing import List


def insert(intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []  #result array to return 

        for i in range(len(intervals)): #iterate thru every single int in the list of ints 
            # edge cases :
            # new int is before curr int : ie new end < curr start 
            if newInterval[1] < intervals[i][0]:
                # then insert new int into the result 
                res.append(newInterval)
                # all ints after that are non overlapping so no need to anything to them, just append them 
                return res + intervals[i:] #sublist from i to end 
            # else new int is after the curr int we are at 
            # i.e new start > curr end 
            # in this case, it could still overlap with some ints on the right 
            # so do not add to the result yet, only append it 
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            # else : curr int is overlapping with new int 
            # so merge ints 
            else:
                newInterval = [
                    min(newInterval[0], intervals[i][0]),
                    max(newInterval[1], intervals[i][1]),
                ]
            # do not add above to result yet since still could overlap 
        
        # in case nonverlapping case does not exec then int will never be added to the result
        # so append new int to result 
        res.append(newInterval)
        return res

print(insert([[1,3],[6,9]],[2,5]))
print(insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]))





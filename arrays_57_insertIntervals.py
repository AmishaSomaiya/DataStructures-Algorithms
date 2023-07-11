"""
https://leetcode.com/problems/insert-interval/
https://www.youtube.com/watch?v=A8NUOmlwOlM

leetcode 57
medium
arrays

input : an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] 
represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. 
You are also given an interval newInterval = [start, end] that represents the start and end of another interval.
output: intervals after the insertion.

Logic : 
-to maintain nonoverlap of intervals, may need to merge if overlap with new interval to be inserted
-intervals already sorted
-overlap at single point counted as overlapped intervals: edge case
-base case 1: to check if an int does not overlap with first interval, it will not overlap
with any other int as well so just insert at beginning
-base case 2: similarly if start value is greater than end of last int, it cannot overlap with any int, so just insert at end
-case 3 : new interval overlaps with multiple intervals -> combine multiple intervals
-case 4 : new interval is somewhere in between 2 intervals and doesnot overlap at all
->
->so iterate thru intervals and find insertion point

Time Complexity: O(n), Space Complexity: O(1)

"""
def insert(intervals, newInterval):
    res = []

    # loop on all intervals
    for i in range(len(intervals)):       
        #nonoverlapping
        if newInterval[1] < intervals[i][0]: # end value of new < startvalue of current
            res.append(newInterval)  #insert new interval into result
            return res + intervals[i:]  #and additional ints can be appended since they are non overlapping
        #nonoverlapping
        elif newInterval[0] > intervals[i][1]:  #start of new int > end of current -> new goes after current int
            res.append(intervals[i])   
        else:
            #new int overlaps with current
            # merge 
            newInterval = [
                min(newInterval[0], intervals[i][0]),
                max(newInterval[1], intervals[i][1]),
            ]
    res.append(newInterval)
    return res

print(insert([[1,3],[6,9]],[2,5]))
print(insert([[1,2],[3,5],[6,7],[8,10],[12,16]],[4,8]))


"""
https://leetcode.com/problems/merge-intervals/
https://www.youtube.com/watch?v=44H3cEC2fFM

leetcode 56
medium
arrays, sorting

input : an array of intervals where intervals[i] = [starti, endi]
output: an array of the non-overlapping intervals that cover all the intervals in the input.

Logic : Sorting intervals can make sure that for any 0 <= i <= size of intervals-1, 
intervals[i][0]<=intervals[i+1][0], so we only need to change end time in overlapping cases.

pseudo-code : 
1. sort intervals by start time
2. loop on intervals:
        get endvalue of most recent interval
        now if start time of current int <= endvalue of prev 
        3. then it means there is an overlap
        then merge them i.e. endvalue of most recent = max(end of current, end of most recent)
        # (1,5) and (2,4) -> (1,5)
        4. when nonoverlapping, take the interval and add it to output



Time Complexity: O(nlogn) because of sorting, Space Complexity: O(1)

"""
def merge(intervals):
        # intervals.sort()
        intervals.sort(key=lambda pair: pair[0])
        output = [intervals[0]]  #so 1 edge case considered


        for start, end in intervals:
            lastEnd = output[-1][1] #end value of most recent interval

            # overlapping case 
            if start <= lastEnd:
                # merge
                output[-1][1] = max(lastEnd, end)
            else:  #nonoverlapping case
                output.append([start, end])
        return output


print(merge([[1,3],[2,6],[8,10],[15,18]]))
print(merge([[1,4],[4,5]]))

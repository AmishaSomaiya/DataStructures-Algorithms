"""
leetcode 253 meeting room II premium
https://www.youtube.com/watch?v=FdzJmTCVyJU&list=PLot-Xpze53lfOdF3KwpMSFEyfE77zIwiP&index=43

leetcode 253
medium
arrays, 2 pointers 

input : array of meeting time intervals of start and end times [[s1,e1], [s2,e2], ... ]
output: return the minimum number of meeting rooms required 

Logic : 

for this prob : 
if e2 = s3, iterate thru end time before start time
ie iterate thru e2 before iterate thru s3 
ie nonoverlapping

approach :
-create 2 sorted arrays for start time and end time separately 
-count var 
-2 pointers : at beginning of start and beginning of end
- pick min between s and e:
if s < e, incre count by 1, shift s pointer 
si < ei 
to return the minimum number of meeting rooms required 
= what is the maximum number of overlapping meetings at any given time 
-maintain a var count : number of active meetings currently
-eg : (0,30), (5,10), (15,20)
-when at si of (5,10), (0,30) is still going on 
 so #active meetings : 2 at this time 
-now at ei of (5,10), (5,10) meeting ended so decre count by 1 

s = (0,5,10) and e = (10,15,30)
    s1,s2,s3          e1,e2,e3
i.e. init s and e pointers at s1,e1
at s1<e1, count = 1 shift s pointer : s2,e1
so now pointers at s2, e1
again s2<e1 : count+= : 2, shift s pointer : s3,e1
now edge case : s2=e1 : tie
so consider e1 < s2 : count -= : 1, shift e pointer : s3,e2
now s3 and e2 : s3<e2 : count+= : 2, shift s pointer: s done, now only e times remain 
so e2 count -= : 1
   e3 count -= : 0
end of both arrays : stop
max count = 2 return 2 

or end of 1 array : stop, do not need to iterate thru entire other array as well

Time Complexity: O(nlogn), s: O(n)

"""

from typing import List

# class Interval(object):
#     def __init__(self, start, end):
#           self.start = start
#           self.end = end 
      
# class Solution: 
#     def minMeetingRooms(intervals: List[List[int]]) -> int:
#         start = sorted([i.start for i in intervals])
#         end = sorted ([i.end for i in intervals])
        
#         res,count = 0, 0

#         s,e = 0,0 #2 pointers 

#         while s<len(intervals):
#                 if start[s] < end[s] :
#                     s+=1
#                     count +=1
#                 else:
#                     e += 1
#                     count -= 1
#                 res = max(res,count)
#         return res 

##########                        

def minMeetingRooms(intervals: List[List[int]]) -> int:
        time = []
        for start, end in intervals:
            time.append((start, 1))
            time.append((end, -1))
        
        time.sort(key=lambda x: (x[0], x[1]))
        
        count = 0
        max_count = 0
        for t in time:
            count += t[1]
            max_count = max(max_count, count)
        return max_count

print(minMeetingRooms([(0,30), (5,10), (15,20)]))
# answer 2

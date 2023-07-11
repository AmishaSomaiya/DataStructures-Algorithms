"""
https://leetcode.com/problems/course-schedule-ii/
https://www.youtube.com/watch?v=Akt3glAwyfY&list=PLot-Xpze53lfOdF3KwpMSFEyfE77zIwiP&index=23

leetcode 210
medium
graph problem 

input : there are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. 
You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.
For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
output: Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. 
If it is impossible to finish all courses, return an empty array.

Logic : 
-first to see if it is even possible, then return the order
-starting at every single node, run dfr on it.
-before that build an adjacency list and know its neighbors
i.e. prereq map

topological sorting :
-start from the node which does not have any inward edges : no prereqs
-add it to output
-cross it out because we r not required to visit it again
-continue similarly
Time Complexity: O(m+n) = #edges+nodes = #prereqs+courses 

how to detect cycle : if repeat node encountered :
using hashset to store current path to know this

if cycle detected : return immediately 

"""

def findOrder(numCourses, prerequisites):
        prereq = {c: [] for c in range(numCourses)}  #empty adjacency list of prereqs 
        for crs, pre in prerequisites: #iterate thru prereq-course pair in given prerequisites 
            prereq[crs].append(pre) #append prereq to corres course

        # 3 states for a course : visited, visiting, unvisited 
        output = []
        visit, cycle = set(), set()

        def dfs(crs):  #pass only the course number currently visiting
            if crs in cycle:
                return False #and terminate and thus return empty list 
            if crs in visit:
                return True  #not to stop the algo but not to visit it again 

            cycle.add(crs) #add course to path(cycle) 
            for pre in prereq[crs]: #recursively run dfs on prereq
                if dfs(pre) == False:  #cycle detected then return false down 
                    return False
            cycle.remove(crs)    #after running the dfs, remove course from the cycle because no longer on the current path 
            visit.add(crs)       #we went thru this course and all of its prereq
            output.append(crs)   #prereqs met so add course to output 
            return True  

        for c in range(numCourses):  #now code execution, run dfs on each course 
            if dfs(c) == False:
                return []   #if cycle detected 
        return output

print(findOrder(2, [[1,0]]))
print(findOrder(4, [[1,0],[2,0],[3,1],[3,2]]))
print(findOrder(1, []))

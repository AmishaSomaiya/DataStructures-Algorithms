"""
https://leetcode.com/problems/course-schedule/
https://www.youtube.com/watch?v=EgI5nU9etnU


leetcode 207
medium
graphs

input : numberofcourses:int, list of lists of prereqs(ints)
output: boolean doable or not

Logic : DFS 
By performing a DFS, we can determine whether this graph is a DAG (Directed Acyclic Graph) 
or not. If so, we can finish all courese (should return True).

pseudo-code : 
1. make a hashtable key=course, value=list of prereqs
   empty list as value if a particular course does not have any prepreq
   -> this course can be completed
        create a defaultdict of type list
        loop on prereqs : 
        list in prereqs = [course, prereq] = [dest,src] 
        defaultdict[src].append(dest)
2. perform DFS on all nodes 
        recursively on all  
        till empty list encountered -> flag can be completed
        remove this course 
3. go backwards 
        mark that this can be completed
        and remove from list
so whenever prereq list is empty -> that course can be completed
4. if all course can be completed -> return true

Time Complexity: O(V + E), Space Complexity: O(V + E), 
where V is the total number of courses and E is the total number of prerequisites.

"""
from typing import List

def canFinish(numCourses: int, prerequisites: List[List[int]]) -> bool:
    # create an initial empty list of prereqs
    # mapping for each course to its pre-req list
    premap = {i:[] for i in range(numCourses)}

    # loop over the nested list variable prerequisites 
    # to get the prerequisites pair(course,prereq) for each course from this list 
    for course, prereq in prerequisites:
        premap[course].append(prereq)

    # create a set that will initially be empty then it will store
    # all the courses along the current DFS path
    visitSet = set()

    # recursively to call dfs so define its function

    def dfs(course):
        # base cases : 
        # 1. if course is already visited : then a loop detected, so cannot be 
        # completed -> return false
        if course in visitSet:
            return False
        
        # 2. if no prereqs, then can be completed -> return True
        if premap[course] == []:
            return True
        
        # else:
        # add this course to the visitset and recursively run dfs on it
        # and its prepreqs
        visitSet.add(course)    
        for prereq in premap[course]:
            if not dfs(prereq): 
                return False #even if 1 course cannot be completed, it is not doable so return False
        # else: remove from visitset,set its premap to empty list,  return true
        visitSet.remove(course)
        premap[course] = []
        return True
    

    for courseno in range(numCourses):
        # loop on all courses
        # because can be indp links like 1->2, 3-> 4
        # check dfs for all courses, even if 1 not true, return false
        # if true for all, return true
        if not dfs(course) : return False
    return True 


print(canFinish(2, [[1,0]]))
print(canFinish(2, [[1,0],[0,1]]))

        






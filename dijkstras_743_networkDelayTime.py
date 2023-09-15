"""
https://leetcode.com/problems/network-delay-time/
https://www.youtube.com/watch?v=EaphyqKU4PQ&list=PLot-Xpze53lfOdF3KwpMSFEyfE77zIwiP&index=72

leetcode 743
medium
djikstra's

input : a network of n nodes, labeled from 1 to n and  also given times, a list of travel times as
directed edges times[i] = (ui, vi, wi), where ui is the source node, vi is the target node, and wi 
is the time it takes for a signal to travel from source to target.

output: minimum time it takes for all the n nodes to receive the signal. 

Logic : to find min time=edges i.e. to find shortest path = dijkstra's algo
= performs BFS = implemented in code using min heap = priority queue

djik algo :
graph algo
- for every node, finds shortest path from source node
-shortest path = min total weight and not min num of nodes passed
to reach the destination
-so each node being visited add to heap

in min heap : track 2 values : path length, since it is used to determine what to pop
based on path length 
2nd value : node being reached
start iwith 0,1 in the ex
step 2 : pop this value
step3 " do bfs, add neighbor to min heap
step 4 : add more neighbor 
..
max value = 3 in eg = to be returnrf




Time Complexity: O(E * logV)
to get min from min heap :logn operation


"""

from collections import defaultdict
import heapq
from typing import List


def networkDelayTime(times: List[List[int]], n: int, k: int) -> int:
        edges = defaultdict(list)  #hashmap of edges, init empty list 
        for u, v, w in times:  #for every edge u in the input 
            edges[u].append((v, w))  #get list of all neiighbors for u, v : neighbor node and w : weight of that node 

        # init minheap with the 1st value, given as k 
        minHeap = [(0, k)]
        visit = set()  #hashset to track visited nodes, we dont want to go in a loop 
        t = 0  #result , final will be cost to visit the last node 
        while minHeap:  #till minheap is not empty 
            w1, n1 = heapq.heappop(minHeap)  #keep popping weight and node 
            if n1 in visit:  #process only if not visited, if visited continue 
                continue
            visit.add(n1)  #if not visited, add to visited 
            t = w1  #update result, weight = time to reach a node 

            # bfs 
            # go thru all neighbors of the node ie in edges[n1]
            for n2, w2 in edges[n1]:
                if n2 not in visit:  #for all neighbors not visited yet 
                    heapq.heappush(minHeap, (w1 + w2, n2))  #add to heap , add to w1 to track total path 
        return t if len(visit) == n else -1  #after the loop, result in t if possible ie if every node visited ie length=total # nodes, else return -1 


print(networkDelayTime([[2,1,1],[2,3,1],[3,4,1]],4,2))
print(networkDelayTime([[1,2,1]],2,1))
print(networkDelayTime([[1,2,1]],2,2))


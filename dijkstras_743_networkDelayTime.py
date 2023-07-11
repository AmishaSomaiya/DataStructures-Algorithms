"""
https://leetcode.com/problems/network-delay-time/
https://www.youtube.com/watch?v=EaphyqKU4PQ&list=PLot-Xpze53lfOdF3KwpMSFEyfE77zIwiP&index=72

leetcode 743
medium
dijkstra's

input : 
output: 

Logic : 


Time Complexity: O(E * logV)

expl todo
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


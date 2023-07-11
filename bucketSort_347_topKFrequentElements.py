"""
https://leetcode.com/problems/top-k-frequent-elements/
https://www.youtube.com/watch?v=YPTqKIgVk-k&list=PLot-Xpze53lfOdF3KwpMSFEyfE77zIwiP&index=60

leetcode 347
medium
bucket search 

input : an integer array nums and an integer k
output: return the k most frequent elements. You may return the answer in any order.

Logic : 
k !> #distinct eles in nums 
input array always nonempty

approach 1 : o(nlogn)
sort entirely
Time Complexity: if all n values are distinct and k=n then time = nlogn

approach 2 : o(klogn)
do not need to sort entirely since we need only top k freq eles
use a max heap : 
i.e. count occurrence of each distinct ele (then no need to sort)
add each pair i.e. ele and #occurrences in the max heap 
where key : #occurrences 
-pop k times 
adding to heap : heapify : linear time : o(n)
pop k times : each pop : O(log n)= o(klogn) = better than o(nlogn)

approach 3 : o(n) if input : bounded 
what wont work: 
bucket sort 
input : indices and value = count of occurrences 
but here input : unbounded (values of eles)
also not clear which top k to pop 

another bucket sort that will work here:
index = count
value = list of eles that have that count = that index 
size of this array = size of nums because worst case all distinct eles
so can scan in linear time 
from top index to lower : top k 

incase all eles are distinct : 
will need to scan entire this bucket sort array : o(n)
+ o(n) once again thru the list at index 1 position : o(n) again
: added : o(n) : still linear 

also hashmap needed to compute occurrences : so space : o(n) also 


"""

from typing import List
def topKFrequent(nums: List[int], k: int) -> List[int]:
        count = {}  #hashmap to count occurrences of values 
        freq = [[] for i in range(len(nums) + 1)] #bucket sort array of size same as nums array 

        for n in nums:
            count[n] = 1 + count.get(n, 0)  #count occurrences 
        for n, c in count.items():  #go thru each value occurred, 
            freq[c].append(n)   #count = index, append the ele to the list at that index  
            # above i.e. this count occurs c number of times 

        res = []  #result of top k elements 
        for i in range(len(freq) - 1, 0, -1):  #from last index to get most freq eles 
            for n in freq[i]:  #go thru every value : could be empty or can have values 
                res.append(n)   
                if len(res) == k:  #stop when k values received 
                    return res  #guaranteed to execute so no need of return outside of loop 

        # O(n)

print(topKFrequent([1,1,1,2,2,3],2))
print(topKFrequent([1],1))

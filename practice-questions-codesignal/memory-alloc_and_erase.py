'''
Given an array of integers memory consisting of 0s and 1s which indicate whether the corresponding memory unit is free or not. 
Memory[i] = 0 means free 1 means occupied. 
Memory is aligned with segments of 8 units so all occupied memory blocks start at index divisible by 8. Eg 0, 8, 16 etc. 
perform 2 types of queries: alloc x : find leftmost aligned memory block of c consecutive free memory units and mark these as occupied. 
If no such proper aligned memory blcok return -1. 
Else return index of 1st position of this. 
Assign id to each element based on atomic counter(starts at 1, incre by 1 for every successful operation).  
X can be greater than 8. 
Second query: erase id: if there is an allocated memory block woth ele ids equal to id, free all mem units and return length if deleted block, if no such block or blvok already deleted, return -1. 
Input is queries : array of 2 ele arrays is second ele of array in this query[i][0] is 0 it is query alloc and if 1 then erase query. And id is queries[i][1] return an array containing results of all queries. 
Input is memory and queries

'''



"""
https://leetcode.com/problems/lru-cache/
https://www.youtube.com/watch?v=7ABFKPK2hD4&list=PLot-Xpze53lfOdF3KwpMSFEyfE77zIwiP&index=27

leetcode 146
medium

input : Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.
output: 
Implement the LRUCache class:
LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
int get(int key) Return the value of the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
The functions get and put must each run in O(1) average time complexity.

Logic : 
-get in O(1) time : so use hashmap with key=node value and value=pointer to that node
-when a value is 'get', it becomes the most recently used value
-the other value becomes the least used value
in eg 1, capacity = 2 so for tracking the most recent and the least recent :
2 pointers : left and right to be used 
- so we are going to maintain an ordered list : so use a linked list
-a doubly linked list 
-if a new item to be put and cache is already at full capacity, then remove the least recently used value
-replace with the new value in the hashmap and have bth pointers in doubly linked list with new value instead of old, point to each other 


-keep track of capacity
-have a hashmap and a doubly linked list 
-each node will have value and 2 pointers : prev and next 
Time Complexity: 

"""

# node has value and 2 pointers : prev and next 
class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None



class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}  # hashmap key to node

        # left : LRU, right : most recent 
        self.left, self.right = Node(0, 0), Node(0, 0)  #left and right pointers 
        self.left.next, self.right.prev = self.right, self.left #initially we want left and right to be connected and new node we want to put in the middle 

    # helper functions : remove and insert 
    # remove node from list
    # pointer of prev to curr deleted and made to point to next 
    # and next to prev since doubly linked list 
    # so current deleted 
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev
    

    # insert node at rightmost position of list
    # prev to next right now 
    # make it as prev->curr-> next and vice versa for doubly ll
    # so both point to middle/current 
    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev

    # return value if key exists in hashmap, else return -1 
    # whenever get, update this node to most recent 
    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])  #remove and reinsert at the rightmost to make most recent used 
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    # if key in map already exists: first remove this node from the list
    # then create a new node with key, value and put it in hashmap
    # and into the doubly linked list. 
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        # if cap exceeded, remove the lru from cache i.e. hashmap
        # where lru = node pointed by left pointer = left.next 
        if len(self.cache) > self.cap:
            # remove from the list and delete the LRU from hashmap
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


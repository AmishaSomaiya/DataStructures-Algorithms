"""
https://leetcode.com/problems/word-ladder/

leetcode 127
hard
graphs

input : beginword, endword, wordlist
output: length of this sequence and 0 if this seq does not exist

Logic : BFS 

pseudo-code : 
make a set of wordlist
declare a deque of 2 elements : beginword and count=0
loop on deque : 
    popleft deque and store the begin word and count in vars
    if begin word same == end word:
        return count +1
    loop on word : 
        loop on ascii :
            form new word by changing single char of word
            new_word = word[:i] + char + word[i+1:]
            check if new_word in set :
                if yes, then remove this word from the set
                append new word and incremented count to deque
return 0 

Time complexity : O(N.M^2)
Space complexity: O(N)

where N is the length of wordList and M is the length of word

"""
from typing import List
from collections import deque
from string import ascii_lowercase

def ladderLength(beginWord, endWord, wordList):

    myset = set(wordList)
    queue = deque([(beginWord, 0)])

    while queue:
        word, count = queue.popleft()
        if word == endWord:
            return count + 1
        for i in range(len(word)):
            for char in ascii_lowercase:
                newWord = word[:i] + char + word[i+1:]
                if newWord in myset :
                    myset.remove(newWord)
                    queue.append((newWord,count+1))
    return 0


print(ladderLength("hit", "cog", ["hot","dot","dog","lot","log","cog"]))
print(ladderLength("hit", "cog", ["hot","dot","dog","lot","log"]))
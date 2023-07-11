"""
https://leetcode.com/problems/implement-trie-prefix-tree/
https://www.youtube.com/watch?v=oobqoCJlHA0&list=PLot-Xpze53lfOdF3KwpMSFEyfE77zIwiP&index=48

leetcode 208
medium

input , output: 
Implement the Trie class:

Trie() Initializes the trie object.
void insert(String word) Inserts the string word into the trie.
boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.

applications : autocomplete, spellchecker 
Logic : 
3 functions : insert, search, checkif starts with prefix 

-for insert=> create a new node for every char as children to children to the starting char 
-mark the end of the word

-for search=> start from start of word, and see if it the next char as the child
the last char in the word to be searched should be marked as complete
else return false

-startwith=> check if first few chars on a branch in the tree match with the given prefix 

insert and search can be done in o(1) time in hashmap or hashset : but cannot implement startswith in hashmap

when a new word inserted with common chars from another word already inserted, a completely new branch is not created
instead ape will be inserted in apple with ap common then a new branch is created for e and e marked as stop node 

-another reason why a trie is useful :
suppose a list of a million records and to search startswith(B), we will need to go thru entire list 
every time we want to search something: but trie is more efficient in that case : worst case : 26 chars so 26 and not a million :O(1)

Time Complexity: o(1) for finding prefix 

"""
class TrieNode:
    def __init__(self):
        self.children = [None] * 26  #can have 26 children 
        self.end = False  #marking each as not end of word by default

class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()  #only from root node, its empty right now 

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        curr = self.root  #start from root 
        for c in word:#loop char by char in word
            i = ord(c) - ord("a")
            if curr.children[i] == None:  #if this char is not in current node's children i.e. not inserted yet 
                curr.children[i] = TrieNode()#then create a trienode for it 
            # else if it already exists then just set current to that child 
            curr = curr.children[i]
        # after end of loop: current is set to last char of word so now end set to true 
        curr.end = True



    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        curr = self.root  #start from root 
        for c in word: #go char by char
            i = ord(c) - ord("a")
            if curr.children[i] == None:  #if doesnt exist, return false 
                return False
            curr = curr.children[i]  #if it exists, move ahead, shift pointer to child pointer 
        return curr.end  #end set to true then it is a word 

    def startsWith(self, prefix: str) -> bool:  #same as search but do not need to check if end or not 
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        curr = self.root
        for c in prefix:
            i = ord(c) - ord("a")
            if curr.children[i] == None:
                return False
            curr = curr.children[i]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
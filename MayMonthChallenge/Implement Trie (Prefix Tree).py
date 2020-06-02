""" Implement Trie (Prefix Tree)
Solution
Implement a trie with insert, search, and startsWith methods.

Example:

Trie trie = new Trie();

trie.insert("apple");
trie.search("apple");   // returns true
trie.search("app");     // returns false
trie.startsWith("app"); // returns true
trie.insert("app");   
trie.search("app");     // returns true
Note:

You may assume that all inputs are consist of lowercase letters a-z.
All inputs are guaranteed to be non-empty strings.


Solution:
"""
class Trie:

    def __init__(self):
        self.lstTrie = []
       
        

    def insert(self, word: str) -> None:
        self.lstTrie.append(word)
        

    def search(self, word: str) -> bool:
        return True if word in self.lstTrie else False

    def startsWith(self, prefix: str) -> bool:
        templst = [x for x in self.lstTrie if prefix in x]
        for x in templst:
            if(x[0:len(prefix)] == prefix):
                return True
            
        else:
            return False
        
        
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
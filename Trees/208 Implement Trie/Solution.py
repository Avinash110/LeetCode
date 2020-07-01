class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = {}
        

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        trie = self.trie
        for w in word:
            if w in trie:
                trie = trie[w]
            else:
                trie[w] = {}
                trie = trie[w]
        
        trie["*"] = {}
        

    def helper(self, word, isFull):
        
        trie = self.trie
        for w in word:
            if w in trie:
                trie = trie[w]
            else:
                return False
            
        if isFull:
            if "*" in trie:
                return True
            else:
                return False
        else:
            return True
        
    
    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        return self.helper(word, True)
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        return self.helper(prefix, False)
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
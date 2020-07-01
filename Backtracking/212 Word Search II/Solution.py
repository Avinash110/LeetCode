class Solution:
    def findWords(self, board, words):
        
        
        self.trie = {}
        
        self.populateTrie(words)
        self.output = set()
        for i in range(len(board)):
            for j in range(len(board[i])):
                self.helper(i, j, board, self.trie, '')
        
        return list(self.output)
    
    
    def helper(self, row, col, board, trie, word):
        
        if "*" in trie:
            self.output.add(word)
            
        if not (row >= 0 and row < len(board) and col >= 0 and col < len(board[0])):
            return
        letter = board[row][col]
        if letter not in trie or letter == "#":
            return
        
        board[row][col] = "#"
        word = word + letter
        dirs = [(1,0), (0,1), (-1, 0), (0, -1)]
        for dx, dy in dirs:
            
            newX = row + dx
            newY = col + dy
            self.helper(newX, newY, board, trie[letter], word)
        
        
        board[row][col] = letter
        
    def populateTrie(self, words):
        
        for word in words:
            trie = self.trie
            for w in word:
                if w in trie:
                    trie = trie[w]
                else:
                    trie[w] = {}
                    trie = trie[w]

            trie["*"] = {}
        
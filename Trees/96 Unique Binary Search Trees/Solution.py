class Solution:
    def numTrees(self, n: int) -> int:
        self.cache = {}
        return self.helper(n)
    
    def helper(self, n):
        if n <= 0:
            return 1
        
        if n <= 2:
            return n
        
        if n in self.cache:
            return self.cache[n]
        
        totalTrees = 0
        for i in range(1, n+1):
            leftTrees = self.helper(i-1)
            rightTrees = self.helper(n-i)
            
            totalTrees += (leftTrees * rightTrees)
        
        self.cache[n] = totalTrees
        return totalTrees
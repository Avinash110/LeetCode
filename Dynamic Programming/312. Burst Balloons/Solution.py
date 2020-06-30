class Solution:
        
    def maxCoins(self, nums) -> int:
        self.cache = {}
        return self.helper(nums, 0, len(nums) - 1)
    
    def helper(self, nums, start, end):
        
        if start > end:
            return 0
        
        if start in self.cache and end in self.cache[start]:
            return self.cache[start][end]
        
        maxCoins = float("-inf")
        
        def get(i , arr):
            if i == -1 or len(arr) == i:
                return 1
            return arr[i]
            
        
        for i in range(start, end+1):
            leftCoins = self.helper(nums, start, i-1)
            rightCoins = self.helper(nums, i+1, end)
            
            currentBurst = get(start-1, nums) * get(i, nums) * get(end+1, nums)
            
            maxCoins = max(maxCoins, leftCoins + rightCoins + currentBurst)
            
        if start not in self.cache:
            self.cache[start] = {}
        self.cache[start][end] = maxCoins
        return maxCoins
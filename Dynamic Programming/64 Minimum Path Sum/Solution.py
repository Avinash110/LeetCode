class Solution:
    def minPathSum(self, grid) -> int:
        
        if not grid or not grid[0]:
            return 0
        
        dp = [[0 for i in range(len(grid[0]) + 1)] for _ in range(len(grid) + 1) ]
        for i in range(1, len(grid) + 1):
            for j in range(1, len(grid[0]) + 1):
                minValue = 0
                if i == 1:
                    minValue = dp[i][j-1]
                elif j == 1:
                    minValue = dp[i-1][j]
                else:
                    minValue = min(dp[i-1][j], dp[i][j-1])
                
                dp[i][j] = grid[i-1][j-1] + minValue
        
        return dp[-1][-1]
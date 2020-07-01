class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        dp = [[0 for _ in range(len(word2) + 1)] for _ in range(len(word1) + 1)]
        
        for i in range(len(word1) + 1):
            dp[i][0] = i
        
        for j in range(len(word2) + 1):
            dp[0][j] = j
        for i,ch1 in enumerate(word1):
            for j,ch2 in enumerate(word2):
                
                if ch1 == ch2:
                    dp[i+1][j+1] = dp[i][j]
                else:
                    # dp[i][j] = replace
                    # dp[i+1][j] = replace
                    # dp[i][j+1] = replace
                    dp[i+1][j+1] = 1 + min(dp[i][j], dp[i+1][j], dp[i][j+1])
                    
        return dp[-1][-1]
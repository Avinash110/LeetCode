class Solution:
    def maxProfit(self, prices) -> int:
        
        minPrice = float("inf")
        
        maxProfit = 0
        
        for n in prices:
            if minPrice > n:
                minPrice = n
            elif n - minPrice > maxProfit:
                maxProfit = n - minPrice
                
        return maxProfit
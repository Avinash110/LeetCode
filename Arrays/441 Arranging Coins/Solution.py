import math
class Solution:
    def arrangeCoins(self, n: int) -> int:
        
        low = int(math.sqrt(n))
        high = n
        
        while low <= high:
            mid = (low + high) // 2
            if mid*mid + mid <= 2*n:
                low = mid + 1
            else:
                high = mid - 1
                
        return low-1
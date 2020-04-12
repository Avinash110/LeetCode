import heapq
class Solution:
    def lastStoneWeight(self, stones) -> int:
        
        stones = [x*-1 for x in stones]
        heapq.heapify(stones)
        
        while len(stones) >= 2:
            
            y = heapq.heappop(stones) * -1
            x = heapq.heappop(stones) * -1
            
            if y > x:
                heapq.heappush(stones, x-y)
        
        return 0 if len(stones) == 0 else stones[0] * -1
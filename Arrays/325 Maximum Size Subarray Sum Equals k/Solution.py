class Solution:
    def maxSubArrayLen(self, nums, k) -> int:
        
        mapSum = {}
        mapSum[0] = -1
        
        rS = 0
        maxL = 0
        for i,n in enumerate(nums):
            rS += n
            if  (rS - k) in mapSum:
                maxL = max(maxL, i - mapSum[rS - k])
            if rS not in mapSum:
                mapSum[rS] = i
        
        return maxL
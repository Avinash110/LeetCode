class Solution:
    def subarraySum(self, nums, k: int) -> int:
        
        sumMap = {0: 1}
        
        count = 0
        
        rS = 0
        for n in nums:
            rS += n
            
            if rS - k in sumMap:
                count += sumMap[rS - k]
            
            sumMap[rS] = sumMap.get(rS, 0) + 1
        
        return count
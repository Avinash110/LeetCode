class Solution:
    def findMaxLength(self, nums) -> int:
        
        if not nums:
            return 0
        
        counts = {0: -1}
        currCount = 0
        maxLength = 0
        for i,n in enumerate(nums):
            if n == 1:
                currCount += 1
            else:
                currCount -= 1
            
            if currCount in counts:
                maxLength = max(maxLength, i - counts[currCount])
            else:
                counts[currCount] = i
        return maxLength
class Solution:
    def maxSubArray(self, nums) -> int:
        
        maxSum = float("-inf")
        currMaxSum = float("-inf")
        for n in nums:
            currMaxSum = max(currMaxSum + n, n)
            maxSum = max(maxSum, currMaxSum)
        return maxSum
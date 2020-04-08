class Solution:
    def moveZeroes(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return nums
        
        nonZeroPointer = 0
        i = 0
        while i < len(nums) :
            while i < len(nums) and nums[i] == 0:
                i += 1
            
            if i == len(nums):
                break
            nums[i], nums[nonZeroPointer] = nums[nonZeroPointer], nums[i]
            i += 1
            nonZeroPointer += 1
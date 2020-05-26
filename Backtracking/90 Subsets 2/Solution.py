class Solution:
	#Time Complexity : N*2^N | Space Complexity : N*2^N
    def subsetsWithDup(self, nums):
        
        self.output = []
        nums.sort()
        self.helper([], nums, 0)
        return self.output
    
    def helper(self, tempList, nums, start):
        
        self.output.append([n for n in tempList])
        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i-1]:
                continue
            tempList.append(nums[i])
            self.helper(tempList, nums, i+1)
            tempList.pop()
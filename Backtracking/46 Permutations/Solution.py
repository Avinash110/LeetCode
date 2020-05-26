class Solution:
	#Time Complexity : n*n! | Space Complexity : n*n!
    def permute(self, nums):
        
        self.output = []
        self.used = {}
        self.helper(nums, [])
        return self.output
    
    def helper(self, nums, tempList):
        if len(tempList) == len(nums):
            self.output.append([n for n in tempList])
            return
        
        for i in range(len(nums)):
            if i in self.used and self.used[i]:
                continue
            
            self.used[i] = True
            tempList.append(nums[i])
            self.helper(nums, tempList)
            self.used[i] = False
            tempList.pop()
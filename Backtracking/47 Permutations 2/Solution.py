class Solution:
    def permuteUnique(self, nums):
        
        self.used = {}
        nums.sort()
        self.output = []
        self.helper(nums, [])
        return self.output
    
    def helper(self, nums, tempList):
        if len(tempList) == len(nums):
            self.output.append([n for n in tempList])
            return 
        
        for i in range(len(nums)):
            if (i in self.used and self.used[i]):
                continue
            
            if i > 0 and nums[i] == nums[i-1] and not self.used.get(i-1, False):
                continue
            
            self.used[i] = True
            tempList.append(nums[i])
            self.helper(nums, tempList)
            self.used[i] = False
            tempList.pop()
class Solution:
	# Using binary counter
    def subsetsUsingBinary(self, nums):
        
        output = []
        length = len(nums)
        for i in range(2**length, 2**(length + 1)):
            binNum = bin(i)
            currSS = []
            for j in range(3, len(binNum)):
                if binNum[j] == "1":
                    currSS.append(nums[j - 3])
            output.append(currSS)
        
        return output

    #Time Complexity: N*2^N | Space Complexity: N*2^N
    def subsetsUsingBacktracking(self, nums):
        self.output = []
        nums.sort()
        self.helper([], nums, 0)
        return self.output
    
    def helper(self, tempList, nums, start):
        self.output.append([n for n in tempList])
        for i in range(start, len(nums)):
            tempList.append(nums[i])
            self.helper(tempList, nums, i+1)
            tempList.pop()
class Solution:
	#Time - O(n) | Space - O(1)
    def productExceptSelf(self, nums):
        
        answer = [1] * len(nums)
        
        prod = nums[0]
        for i in range(1, len(nums)):
            answer[i] = prod
            prod *= nums[i]
        
        prod = nums[-1]
        for i in reversed(range(0, len(nums) - 1)):
            answer[i] *= prod
            prod *= nums[i]
        
        return answer

	#Time - O(n) | Space - O(n)
    # def productExceptSelf(self, nums):
        
    #     leftProd = [1] * len(nums)
    #     rightProd = [1] * len(nums)
        
    #     currentProd = 1
    #     for i in range(1, len(nums)):
    #         currentProd *= nums[i - 1]
    #         leftProd[i] = currentProd
        
    #     currentProd = 1
    #     for i in reversed(range(0, len(nums) - 1)):
    #         currentProd *= nums[i + 1]
    #         rightProd[i] = currentProd
        
    #     output = [1] * len(nums)
    #     for i in range(len(nums)):
    #         output[i] = rightProd[i] * leftProd[i]
        
    #     return output
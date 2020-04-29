# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        
        return self.helper(root)[1]
    
    def helper(self, node):
        
        if not node:
            return [float("-inf"), float("-inf")]
        
        leftSum, leftMax = self.helper(node.left)
        rightSum, rightMax = self.helper(node.right)
        
        maxSum = max(leftSum, rightSum, 0) + node.val
        
        mS = max(leftSum, 0) + max(rightSum, 0)
        return (maxSum, max(leftMax, rightMax, mS + node.val))
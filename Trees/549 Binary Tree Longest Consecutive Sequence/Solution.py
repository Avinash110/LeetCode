# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def longestConsecutive(self, root) -> int:
        
        if not root:
            return 0
        
        self.maxCount = 1
        self.helper(root)
        return self.maxCount
    
    def helper(self, node):
        if not node:
            return (0, 0)
        
        inc = 1
        dec = 1
        if node.left:
            leftInc, leftDec = self.helper(node.left)
            if node.val == node.left.val - 1:
                inc = leftInc + 1
            elif node.val == node.left.val + 1:
                dec = leftDec + 1
        
        if node.right:
            rightInc, rightDec = self.helper(node.right)
            if node.val == node.right.val - 1:
                inc = max(inc, rightInc + 1)
            elif node.val == node.right.val + 1:
                dec = max(dec, rightDec + 1)
        
        self.maxCount = max(self.maxCount, inc + dec -1)
        return (inc, dec)
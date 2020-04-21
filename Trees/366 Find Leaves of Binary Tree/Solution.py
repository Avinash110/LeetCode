# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findLeaves(self, root: TreeNode) -> List[List[int]]:
        
        output = {}
        
        def helper(node):
            
            if not node:
                return 0
            
            leftHeight = 1 + helper(node.left)
            rightHeight =  1 + helper(node.right)
            
            maxHeight = max(leftHeight, rightHeight)
            if maxHeight not in output:
                output[maxHeight] = []
            output[maxHeight].append(node.val)
            
            return maxHeight
        
        helper(root)
        
        return output.values()
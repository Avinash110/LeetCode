# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        if n == 0:
            return []
        return self.helper(1, n)
        
    def helper(self, start, n):
        if n == 0:
            return [None]
        
        if start > n:
            return [None]
        
        output = []
        for i in range(start, n+1):
            
            leftTrees = self.helper(start, i - 1)
            rightTrees = self.helper(i+1, n)
            
            for leftTree in leftTrees:
                for rightTree in rightTrees:
                    root = TreeNode(i)
                    root.left = leftTree
                    root.right = rightTree
                    
                    output.append(root)
        return output
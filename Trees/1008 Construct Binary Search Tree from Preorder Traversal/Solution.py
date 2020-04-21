# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        
        def helper(arr, start, end):
            if start > end:
                return
            
            node = TreeNode(arr[start])
            part = start + 1
            while part <= end and arr[start] > arr[part]:
                part += 1
                
            node.left = helper(arr, start + 1, part - 1)
            node.right = helper(arr, part, end)
            
            return node
            
        
        return helper(preorder, 0, len(preorder) - 1)
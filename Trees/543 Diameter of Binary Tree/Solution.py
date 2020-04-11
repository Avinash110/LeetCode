class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0
        return self.helper(root)[0] - 1
    
    def helper(self, node):
        
        if not node:
            return (0, 0)
        
        leftPath, leftMaxPath = self.helper(node.left)
        rightPath, rightMaxPath = self.helper(node.right)
        
        maxPathAtNode = max(leftPath, rightPath, leftMaxPath + rightMaxPath + 1)
        return (maxPathAtNode, max(leftMaxPath, rightMaxPath) + 1)
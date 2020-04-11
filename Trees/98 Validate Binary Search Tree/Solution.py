class Solution:
	def validateBst(tree):
    # Write your code here.
		return helper(tree, float("-inf"), float("inf"))
		
	def helper(node, leftLimit, rightLimit):
		if not node:
			return True
		elif node.value >= leftLimit and node.value < rightLimit:
			return helper(node.left, leftLimit, node.value) and helper(node.right, node.value, rightLimit)
		else:
			return False
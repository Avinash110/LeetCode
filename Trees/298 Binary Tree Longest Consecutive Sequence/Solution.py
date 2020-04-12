class Solution:

	def longestConsecutive(self, root):

		if not root:
			return 0

		return self.helper(root, None, 0)

	def helper(self, node, target, count):

		if not node:
			return count

		count = 1 if target == None or target != node.val else count + 1
		return max(count, self.helper(node.left, node.val + 1, count), self.helper(node.right, node.val + 1, count))

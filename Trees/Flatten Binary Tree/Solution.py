class Solution:
	def flattenBinaryTree(root):
	    # Write your code here.
		leftMost = None
	    stack = []
		prev = None
		
		curr = root
		while len(stack) or curr != None:
			
			while curr:
				stack.append(curr)
				curr = curr.left
				
			node = stack.pop()
			if leftMost == None:
				leftMost = node
			
			curr = node.right
			
			if prev:
				node.left = prev
				prev.right = node
			
			prev = node
			
		return leftMost
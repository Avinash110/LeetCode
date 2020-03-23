class Solution:
	# Time Complexity - O(n) | Space Complexity - O(n)
    def longestValidParentheses(self, s: str) -> int:
        
        str_copy = list(s)
        
        stack = []
        for i, ch in enumerate(s):
            if ch == "(":
                stack.append(i)
            else:
                if len(stack):
                    str_copy[i] = "1"
                    str_copy[stack[-1]] = "1"
                    stack.pop()
        
        maxCount = 0
        count = 0
        for ch in str_copy:
            if ch == "1":
                count += 1
            else:
                maxCount = max(maxCount, count)
                count = 0
        return max(maxCount, count)
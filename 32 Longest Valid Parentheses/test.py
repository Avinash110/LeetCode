from Solution import Solution 
sol = Solution()

assert(sol.longestValidParentheses(")()") == 2)
assert(sol.longestValidParentheses("()()") == 4)
assert(sol.longestValidParentheses("((())))") == 6)
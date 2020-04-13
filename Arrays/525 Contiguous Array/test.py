from Solution import Solution 
sol = Solution()

assert(sol.findMaxLength([0,1]) == 2)
assert(sol.findMaxLength([0,1,0]) == 2)
assert(sol.findMaxLength([0,0,1,0,0,0,1,1]) == 6)
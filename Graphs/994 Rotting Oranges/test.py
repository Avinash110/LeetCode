from Solution import Solution 
sol = Solution()

assert(sol.orangesRotting([[2,1,1],[1,1,0],[0,1,1]]) == 4)
assert(sol.orangesRotting([[2,1,1],[0,1,1],[1,0,1]]) == -1)
assert(sol.orangesRotting([[0,2]]) == 0)
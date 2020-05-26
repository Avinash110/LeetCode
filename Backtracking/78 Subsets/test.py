from Solution import Solution 
sol = Solution()

assert(sol.subsetsUsingBinary([1,2,3]) == [[],[3],[2],[2,3],[1],[1,3],[1,2],[1,2,3]])
assert(sol.subsetsUsingBacktracking([1,2,3]) == [[],[1],[1,2],[1,2,3],[1,3],[2],[2,3],[3]])
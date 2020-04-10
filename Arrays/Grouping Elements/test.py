from Solution import Solution 
sol = Solution()

assert(sol.grouping([2,1,1,2,1]) == [[1], [2], [0, 3], [4]])
assert(sol.grouping([2,2,2,2]) == [[0,1], [2,3]])
assert(sol.grouping([3,3,2,3,2,1]) == [[0,1,3], [2,4], [5]])
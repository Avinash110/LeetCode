from Solution import Solution 
sol = Solution()

assert(sol.searchInsert([1,3,5,6], 5) == 2)
assert(sol.searchInsert([1,3,5,6], 2) == 1)
assert(sol.searchInsert([1,3,5,6], 7) == 4)
assert(sol.searchInsert([1,3,5,6], 0) == 0)
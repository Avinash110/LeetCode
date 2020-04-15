from Solution import Solution 
sol = Solution()

assert(sol.stringShift("abc", [[0,1],[1,2]]) == "cab")
assert(sol.stringShift("abcdefg", [[1,1],[1,1],[0,2],[1,3]]) == "efgabcd")
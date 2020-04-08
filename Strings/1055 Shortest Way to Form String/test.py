from Solution import Solution 
sol = Solution()

assert(sol.shortestWay("abc", "abcbc") == 2)
assert(sol.shortestWay("abc", "acdbc") == -1)
assert(sol.shortestWay("xyz", "xzyxz") == 3)
assert(sol.shortestWay("aaa", "a") == 1)

assert(sol.binary_search("abc", "abcbc") == 2)
assert(sol.binary_search("abc", "acdbc") == -1)
assert(sol.binary_search("xyz", "xzyxz") == 3)
assert(sol.binary_search("aaa", "a") == 1)
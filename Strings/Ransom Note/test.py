from Solution import Solution 
sol = Solution()

assert(sol.canConstruct("a", "b") == False)
assert(sol.canConstruct("aa", "ab")  == False)
assert(sol.canConstruct("aa", "aab") == True)
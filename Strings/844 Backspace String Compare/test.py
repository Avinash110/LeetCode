from Solution import Solution 
sol = Solution()

assert(sol.backspaceCompare("ab#c", "ad#c") == True)
assert(sol.backspaceCompare("ab##", "c#d#") == True)
assert(sol.backspaceCompare("a##c", "#a#c") == True)
assert(sol.backspaceCompare("a#c", "b") == False)
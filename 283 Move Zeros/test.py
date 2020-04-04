from Solution import Solution 
sol = Solution()

arr = [0,1,0,3,12]
sol.moveZeroes(arr)
assert(arr == [1,3,12,0,0])
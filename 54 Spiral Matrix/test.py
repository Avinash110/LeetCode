from Solution import Solution 
sol = Solution()

arr = [
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]

assert(sol.spiralOrder(arr) == [1,2,3,6,9,8,7,4,5])
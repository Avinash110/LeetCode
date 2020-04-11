from Solution import Solution 
sol = Solution(10)

output = []
expectedOutput = [0,9,4,None ,None ,0,4,2,6,1,3,5,7,8,None ,None ,0,4,None ,7,None ,3,None ,3,None ,9,None ,None ,0,8,None ,None ,0,8,None ]

inputFunc = ["seat","seat","seat","leave0","leave4","seat","seat","seat","seat","seat","seat","seat","seat","seat","leave0","leave4","seat","seat","leave7","seat","leave3","seat","leave3","seat","leave9","seat","leave0","leave8","seat","seat","leave0","leave8","seat","seat","leave2"]
for f in inputFunc:
	if f == "seat":
		output.append(sol.seat())
	else:
		output.append(sol.leave(int(f[-1])))

assert(output == expectedOutput)
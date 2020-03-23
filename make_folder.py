import sys
import os

if len(sys.argv) < 2:
	print("Enter name of the folder")
	sys.exit(0)

name = sys.argv[1]

if not os.path.exists(name):
    os.makedirs(name)
    
    solution_file = os.path.join(name, "Solution.py")
    test_file = os.path.join(name, "test.py")

    with open(solution_file, 'w+') as f:
    	f.write("class Solution:")

    with open(test_file, 'w+') as f:
    	f.write("from Solution import Solution \nsol = Solution()")


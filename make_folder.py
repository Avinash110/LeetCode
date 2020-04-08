import sys
import os
from consolemenu import *
from consolemenu.items import *

if len(sys.argv) < 2:
	print("Enter name of the Problem")
	sys.exit(0)

dirs = [x for x in os.listdir('.') if os.path.isdir(x) and x != ".git"]

folder = dirs[SelectionMenu.get_selection(dirs)]
name = sys.argv[1]
problemDir = os.path.join(folder, name)

if not os.path.exists(problemDir):
    os.makedirs(problemDir)
    
    solution_file = os.path.join(problemDir, "Solution.py")
    test_file = os.path.join(problemDir, "test.py")

    with open(solution_file, 'w+') as f:
    	f.write("class Solution:")

    with open(test_file, 'w+') as f:
    	f.write("from Solution import Solution \nsol = Solution()")


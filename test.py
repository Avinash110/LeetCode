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
print(problemDir)
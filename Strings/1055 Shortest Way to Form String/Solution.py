from bisect import bisect_left
from collections import defaultdict
class Solution:
	def binary_search(self, source: str, target: str) -> int:
		
		charIndexes = defaultdict(list)
		for i, c in enumerate(source):
			charIndexes[c].append(i)
		
		loop_cnt = 1
		i = 0
		for t in target:
			if t not in charIndexes:
				return -1
			
			indexes = charIndexes[t]
			src_index = bisect_left(indexes, i)
			if src_index == len(indexes):
				loop_cnt += 1
				i = indexes[0] + 1
			else:
				i = indexes[src_index] + 1
		
		return loop_cnt
	
	def shortestWay(self, source: str, target: str) -> int:
		
		count = 0
		targetIndex = 0
		while targetIndex < len(target):
			found = False
			for i in range(len(source)):
				if targetIndex < len(target) and source[i] == target[targetIndex]:
					targetIndex += 1
					found = True
			if not found:
				return -1
			count += 1
		return count


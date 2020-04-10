class Solution:
	def grouping(self, counts):
    
	    groups = {}
	    output = []
	    for i, n in enumerate(counts):
	        if n not in groups:
	            groups[n] = []
	            
	        if len(groups[n]) == n - 1:
	            output.append(groups[n] + [i])
	            groups[n] = []
	        else:
	            groups[n].append(i)
	    return output
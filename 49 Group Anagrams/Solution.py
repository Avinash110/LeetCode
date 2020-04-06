class Solution:
	# Time complexity O(N*MlogM) | Space complexity O(NM)
    def groupAnagrams(self, strs):
        anagram = {}
        
        sortedStrings = []
        for i, s in enumerate(strs):
            sortedStrings.append("".join(sorted(s)))
        
        for i, s in enumerate(strs):
            group = anagram.get(sortedStrings[i], [])
            group.append(s)
            anagram[sortedStrings[i]] = group
        
        return list(anagram.values())
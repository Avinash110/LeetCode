class Solution:
	# Time complexity O(N*MlogM) | Space complexity O(1)
    def groupAnagrams(self, strs):
        anagram = {}
        
        for i, s in enumerate(strs):
            sortedString = "".join(sorted(s))
            group = anagram.get(sortedString, [])
            group.append(s)
            anagram[sortedString] = group
        
        return list(anagram.values())
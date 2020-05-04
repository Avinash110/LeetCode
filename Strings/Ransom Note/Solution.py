class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        magMap = {}
        for m in magazine:
            if m not in magMap:
                magMap[m] = 0
            magMap[m] += 1
        
        for r in ransomNote:
            if r not in magMap or magMap[r] <= 0:
                return False
            
            magMap[r] -= 1
        
        
        return True
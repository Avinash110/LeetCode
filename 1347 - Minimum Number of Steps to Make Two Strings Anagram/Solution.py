# Time Complexity - O(n) | Space Complexity - O(1)
class Solution:
    def minSteps(s: str, t: str) -> int:
        
        def makeDict(st):
            dic = {}
            for c in st:
                dic[c] = dic.get(c, 0) + 1
            return dic
        
        sMap = makeDict(s)
        tMap = makeDict(t)
        
        minChange = 0
        for c in tMap:
            tVal = tMap[c]
            sVal = sMap.get(c, 0)
            
            if tVal > sVal:
                minChange += tVal - sVal
        
        return minChange
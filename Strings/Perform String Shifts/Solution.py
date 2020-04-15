class Solution:
    def stringShift(self, s: str, shift) -> str:
        
        overallShift = 0
        for sh in shift:
            if sh[0] == 0:
                overallShift += sh[1]
            else:
                overallShift -= sh[1]
        
        newStr = ""
        for i in range(len(s)):
            index = (i + overallShift) % len(s)
            if index < 0:
                index += len(s)
            newStr += s[index]
        
        return newStr
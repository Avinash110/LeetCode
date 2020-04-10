class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        
        stackS = []
        for s in S:
            if s == "#":
                if len(stackS):
                    stackS.pop()
            else:
                stackS.append(s)
        
        stackT = []
        for t in T:
            if t == "#":
                if len(stackT):
                    stackT.pop()
            else:
                stackT.append(t)
        
        return stackT == stackS
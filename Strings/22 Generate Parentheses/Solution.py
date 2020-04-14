class Solution:
    def generateParenthesis(self, n: int):
        
        self.output = []
        
        self.helper(0, 0, n, "")
        
        return self.output
    
    def helper(self, openP, closeP, n, s):
        if openP > n or closeP > n:
            return
        
        if openP == n and closeP == n:
            self.output.append(s)
            return
        
        if openP < n:
            self.helper(openP+1, closeP, n, s + "(")
        
        if closeP < openP and closeP < n:
            self.helper(openP, closeP+ 1, n, s + ")")
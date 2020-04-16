class Solution:
    def checkValidString(self, s: str) -> bool:
        
        leftBalance = 0
        for c in s:
            if c == "(" or c == "*":
                leftBalance += 1
            else:
                leftBalance -= 1
            
            if leftBalance < 0 :
                return False
        
        if leftBalance == 0:
            return True
        
        rightBalance = 0
        for c in reversed(list(s)):
            if c == ")" or c == "*":
                rightBalance += 1
            else:
                rightBalance -= 1
            
            if rightBalance < 0 :
                return False
        
        return True
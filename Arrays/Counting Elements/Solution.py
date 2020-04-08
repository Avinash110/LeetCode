class Solution:
    def countElements(self, arr) -> int:
        
        numSet = set()
        for n in arr:
            numSet.add(n)
           
        count = 0
        for n in arr:
            if n+1 in numSet:
                count +=1
        return count
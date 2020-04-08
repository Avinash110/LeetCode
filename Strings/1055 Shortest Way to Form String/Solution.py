class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        
        count = 0
        targetIndex = 0
        while targetIndex < len(target):
            found = False
            for i in range(len(source)):
                if targetIndex < len(target) and source[i] == target[targetIndex]:
                    targetIndex += 1
                    found = True
            if not found:
                return -1
            count += 1
        return count
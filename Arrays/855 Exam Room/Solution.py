import bisect
class Solution:

    def __init__(self, N: int):
        
        self.N = N
        self.pos = []

    def seat(self) -> int:
        
        if len(self.pos) == 0:
            self.pos = [0]
            return 0
        
        pos = 0
        maxD = self.pos[0]
        for i in range(1, len(self.pos)):
            currD = (self.pos[i] - self.pos[i-1]) // 2
            if currD > maxD:
                maxD = currD
                pos = self.pos[i-1] + currD
                
        if self.N - 1 - self.pos[-1] > maxD:
            pos = self.N - 1
        
        bisect.insort(self.pos,pos)
        return pos
            

    def leave(self, p: int) -> None:
        self.pos.remove(p)


# Your ExamRoom object will be instantiated and called as such:
# obj = ExamRoom(N)
# param_1 = obj.seat()
# obj.leave(p)
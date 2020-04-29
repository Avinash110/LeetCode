from collections import OrderedDict
class FirstUnique:
    def __init__(self, nums):
        self.numSet = set()
        self.numList = OrderedDict()
        for n in nums:
            self.add(n)

    def showFirstUnique(self) -> int:
        
        if not self.numList:
            return -1
        
        return list(self.numList.keys())[0]

    def add(self, value: int) -> None:
        if value not in self.numSet:
            self.numSet.add(value)
            self.numList[value] = True
        else:
            if  value in self.numList:
                del self.numList[value]
# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)
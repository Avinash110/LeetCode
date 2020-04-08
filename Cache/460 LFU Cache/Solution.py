from collections import OrderedDict
class Node:
    def __init__(self, key, value, freq):
        self.key = key
        self.value = value
        self.freq = freq
        
class LFUCache:

    def __init__(self, capacity: int):
        
        self.max_cap = capacity
        self.cur_cap = 0
        
        self.min_freq = 0
        
        self.keyToNode = dict()
        self.freqToKeyList = defaultdict(OrderedDict)

    def get(self, key: int) -> int:
        
        if key not in self.keyToNode:
            return -1
        
        node = self.keyToNode[key]
        
        del self.freqToKeyList[node.freq][key]
        
        if not self.freqToKeyList[node.freq]:
            del self.freqToKeyList[node.freq]
        
        node.freq += 1
        self.freqToKeyList[node.freq][key] = node
        
        if self.min_freq not in self.freqToKeyList:
            self.min_freq += 1
            
        return node.value
        

    def put(self, key: int, value: int) -> None:
        
        if self.max_cap == 0:
            return
        
        if key in self.keyToNode:
            self.keyToNode[key].value = value
            _ = self.get(key)
            return 
        if self.cur_cap == self.max_cap:
            self.cur_cap -= 1
            _, node = self.freqToKeyList[self.min_freq].popitem(last = False)
            del self.keyToNode[node.key]
        
        node = Node(key, value, 1)
        self.freqToKeyList[1][node.key] = node
        self.keyToNode[node.key] = node
        self.cur_cap += 1
        self.min_freq = 1

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
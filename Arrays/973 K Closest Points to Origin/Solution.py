import heapq
class Solution:
    def kClosestUsingHeap(self, points, K: int):
        def distance(x, y):
            return math.sqrt((x*x) + (y*y)) 
         
        output = []
        
        for x,y in points:
            dist = -distance(x, y)
            if len(output) == K and dist <= output[0][0]:
                continue
            else:
                if len(output) == K and dist > output[0][0]:
                    heapq.heappop(output)
                heapq.heappush(output, (dist, [x,y]))
                    
        
        return list(map(lambda x: x[1], output))

        
    def kClosest(self, points, K: int):
        return self.sort(points, K, 0 , len(points) - 1)
        
    def sort(self, points, K, start, end):
        
        if start > end:
            return
        
        index = self.partition(points, start, end)
        if index == K - 1:
            return points[:K]
        
        elif index > K - 1:
            return self.sort(points, K, start, index - 1)
        else:
            return self.sort(points, K, index + 1, end)
            
    def partition(self, points, start, end):
        
        def distance(x, y):
            return (x*x) + (y*y)
        
        dist = distance(points[end][0], points[end][1])
        pivotIndex = start
        for i in range(start, end):
            if distance(points[i][0], points[i][1]) <= dist:
                points[pivotIndex], points[i] = points[i], points[pivotIndex]
                pivotIndex += 1
        
        points[pivotIndex], points[end] = points[end], points[pivotIndex]
        
        return pivotIndex
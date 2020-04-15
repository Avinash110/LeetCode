class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        rottenOrangesTime = {}
        freshOranges = set()
        
        for i, row  in enumerate(grid):
            for j, n in enumerate(row):
                if n == 2:
                    rottenOrangesTime[str(i)+"-"+str(j)] = 0
                elif n == 1:
                    freshOranges.add(str(i)+"-"+str(j))
        
        minTime = float("inf")
        dirs = [(0,1), (1,0), (0,-1), (-1, 0)]
        
        queue = [(x,0) for x in rottenOrangesTime.keys()]
        
        while len(queue):
            
            cell, time = queue.pop(0)
            if cell in freshOranges:
                freshOranges.remove(cell)
            
            rottenOrangesTime[cell] = min(rottenOrangesTime.get(cell, float("inf")), time)
                
            cell = cell.split("-")
            x, y = cell
            x = int(x)
            y = int(y)
            
            grid[x][y] = 2
            
            for dx, dy in dirs:
                newX = x + dx
                newY = y + dy
                
                if newX>= 0 and newY>=0 and newX< len(grid) and newY < len(grid[0]) and  grid[newX][newY] == 1:
                    queue.append((str(newX)+"-"+str(newY), time + 1))
        
        if len(freshOranges):
            return -1
        else:
            values = rottenOrangesTime.values()
            if len(values):
                return max(values)
            else:
                return 0
            # return max()
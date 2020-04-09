class Solution:
    def findMinDifference(self, timePoints) -> int:
        
        minutes = []
        for t in timePoints:
            hours, mins = t.split(":")
            hours = int(hours)
            mins = int(mins)
            
            minutes.append(hours*60 + mins)
        
        minutes.sort()
        
        minMinutes = 2000
        for i in range(1, len(minutes)):
            minMinutes = min(minMinutes, minutes[i] - minutes[i-1])
        
        minMinutes = min(minMinutes, (minutes[0] + 1440)- minutes[-1] )
        
        return minMinutes
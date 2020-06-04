class Solution:
    def twoCitySchedCost(self, costs):
        
        totalCostOfA = sum([x[0] for x in costs])
        
        costs.sort(key=lambda x : x[1] - x[0])
        for i in range(len(costs) // 2):
            totalCostOfA = totalCostOfA - costs[i][0] + costs[i][1]
        
        return totalCostOfA
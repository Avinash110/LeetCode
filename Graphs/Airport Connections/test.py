from Solution import Solution 
sol = Solution()

assert(sol.airportConnections(["BGI","CDG","DEL","DOH","DSM","EWR","EYW","HND","ICN","JFK","LGA","LHR","ORD","SAN","SFO","SIN","TLV","BUD"], [["DSM", "ORD"],["ORD", "BGI"],["BGI", "LGA"],["SIN", "CDG"],["CDG", "SIN"],["CDG", "BUD"],["DEL", "DOH"],["DEL", "CDG"],["TLV", "DEL"],["EWR", "HND"],["HND", "ICN"],["HND", "JFK"],["ICN", "JFK"],["JFK", "LGA"],["EYW", "LHR"],["LHR", "SFO"],["SFO", "SAN"],["SFO", "DSM"],["SAN", "EYW"]], "LGA") == 3)
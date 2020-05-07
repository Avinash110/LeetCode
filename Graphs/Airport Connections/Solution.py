class Solution:
	def airportConnections(self, airports, routes, startingAirport):
	    # Write your code here.
	    airportGraph = createAirportGraph(airports, routes)
		unreachableAirports = getUnreachableAirports(airportGraph, airports, startingAirport)
		markUnreachableAirports(airportGraph, unreachableAirports)
		return getMinNUmberOfConnections(airportGraph, unreachableAirports)

	def getMinNUmberOfConnections(airportGraph, unreachableAirports):
		unreachableAirports.sort(key= lambda x: len(x.unreachableConnections), reverse=True)
		count = 0
		for airportNode in unreachableAirports:
			if airportNode.isReachable:
				continue
			count += 1
			for unreachableConnection in airportNode.unreachableConnections:
				unreachableConnection.isReachable = True
		return count
		
	def markUnreachableAirports(airportGraph, unreachableAirports):
		for airportNode in unreachableAirports:
			
			unreachableConnections = []
			depthFirstTraverse2(airportGraph, airportNode, unreachableConnections, {})
			airportNode.unreachableConnections = unreachableConnections
			
	def depthFirstTraverse2(airportGraph, airport, unreachableConnections, visited):
		
		if airport.isReachable or airport in visited:
			return
		visited[airport] = True
		unreachableConnections.append(airport)
		for connection in airport.connections:
			depthFirstTraverse2(airportGraph, airportGraph[connection], unreachableConnections, visited)
			
	def getUnreachableAirports(airportGraph, airports, startingAirport):
		visited = {}
		depthFirstTraverse(airportGraph, startingAirport, visited)
		
		unreachableAirports = []
		for airport in airports:
			if airport in visited:
				continue
			airportGraph[airport].isReachable = False
			unreachableAirports.append(airportGraph[airport])
		
		return unreachableAirports

	def depthFirstTraverse(airportGraph, airport, visited):
		if airport in visited:
			return
		visited[airport] = True
		for connection in airportGraph[airport].connections:
			depthFirstTraverse(airportGraph, connection, visited)
		
	def createAirportGraph(airports, routes):
		airportGraph = {}
		for airport in airports:
			airportGraph[airport] = AirportNode(airport)
		
		for airport, connection in routes:
			airportGraph[airport].connections.append(connection)
		
		return airportGraph
	
class AirportNode:
	def __init__(self, airport):
		self.airport = airport
		self.isReachable = True
		self.connections = []
		self.unreachableConnections = []
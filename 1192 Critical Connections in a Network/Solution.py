from collections import defaultdict
class Solution:
	def getCriticalConnections(self, n, connections):

		graph = defaultdict(list)
		for con in connections:
			graph[con[0]].append(con[1])
			graph[con[1]].append(con[0])

		low = [n] * n
		self.criticalConnections = []

		def dfs(node, discovery_time, parent):
			if low[node] == n:
				low[node] = discovery_time

				for neigh in graph[node]:
					if neigh != parent:
						expected_discovery_time = discovery_time + 1
						actual_discovery_time = dfs(neigh, expected_discovery_time, node)

						if actual_discovery_time >= expected_discovery_time:
							self.criticalConnections.append([node, neigh])

						low[node] = min(low[node], actual_discovery_time)
			return low[node]

		dfs(0, 0, -1)
		return self.criticalConnections
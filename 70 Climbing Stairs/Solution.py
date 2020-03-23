class Solution:
	# Time Complexity - O(2^n) | Space Complexity - O(n)
	def recursion(self, n):
		self.cache = {}
		return self.recursionHelper(0, n)

	def recursionHelper(self, i ,n):
		if i > n:
			return 0
		if i == n:
			return 1

		if i in self.cache:
			return self.cache[i]

		ways = self.recursionHelper(i+1, n) + self.recursionHelper(i+2, n)
		self.cache[i] = ways
		return self.cache[i]


	# Time Complexity - O(n) | Space Complexity - O(n)
	def ways_dp(self, n):
		if n < 2:
			return 1
		dp = [1] * (n+1)
		for i in range(2, n+1):
			dp[i] = dp[i-1] + dp[i-2]
		return dp[n]

	# Time Complexity - O(n) | Space Complexity - O(1)
	def ways_dp_optimized(self, n):
		if n < 2:
			return 1
		first = 1
		second = 1
		for i in range(2, n+1):
			ways = first + second
			first = second
			second = ways
		return second
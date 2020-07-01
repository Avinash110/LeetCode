from Solution import Solution 
sol = Solution()

board = [
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]

res = sol.findWords(board, ["oath","pea","eat","rain"])
assert(res == ['oath', 'eat'])
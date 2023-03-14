import sys
sys.setrecursionlimit(10**6)
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        n,m = len(matrix),len(matrix[0])
        dp = [[-1]*m for _ in range(n)]
        # x,y 값과 이전의 값들을 비교하여 계산한다.
        # dfs(x,y) := x,y 까지왔을때 최대 길이 
        def dfs(x,y):
            ret = dp[x][y]
            if ret != -1 : return ret
            val = matrix[x][y]
            dp[x][y] = 1 + max(
                dfs(x - 1,y) if x - 1 >= 0 and val > matrix[x - 1][y] else 0,
                dfs(x + 1,y) if x + 1 < n and val > matrix[x + 1][y] else 0,
                dfs(x,y - 1) if y - 1 >= 0 and val > matrix[x][y - 1] else 0,
                dfs(x,y + 1) if y + 1 < m and val > matrix[x][y + 1] else 0 
            )
            return dp[x][y]
        return max(dfs(x,y) for y in range(m) for x in range(n))
        
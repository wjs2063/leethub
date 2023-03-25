class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        n,m = m,n
        dp = [[0]*m for _ in range(n)]
        dp[0][0] = 1
        for i in range(n):
            for j in range(m):
                if i == 0 or j == 0 :
                    dp[i][j] = 1
                    continue
                if j - 1 >= 0 :
                    dp[i][j] += dp[i][j - 1]
                if i - 1 >= 0 :
                    dp[i][j] += dp[i - 1][j]
        return dp[-1][-1]
        
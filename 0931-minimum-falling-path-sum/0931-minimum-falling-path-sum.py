class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        from heapq import heappush,heappop
        n = len(matrix)
        INF = int(1e10)
        dp = [[INF]*n for _ in range(n)]
        for i in range(n):
            dp[0][i] = matrix[0][i]
        for i in range(1,n):
            for j in range(n):
                for ny in [j - 1,j,j + 1]:
                    if 0 <= ny < n:
                        dp[i][j] = min(dp[i - 1][ny] + matrix[i][j],dp[i][j])
        return min(dp[n - 1])
            
class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        INF = int(1e10)
        dp = [[INF]*n for _ in range(n)]
        grp = [[] for _ in range(n)]
        for x,y,c in edges:
            grp[x].append((c,y))
            dp[x][y] = c
            dp[y][x] = c
        for i in range(n):
            dp[i][i] = 0
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    dp[i][j] = min(dp[i][j],dp[i][k] + dp[k][j])
        ans = [set() for _ in range(n)]
        m = int(1e10)
        answer = 0
        for i in range(n):
            for j in range(n):
                if i == j :continue
                if dp[i][j] <= distanceThreshold:
                    ans[i].add(j)
                    ans[j].add(i)
            if len(ans[i]) <= m:
                m = len(ans[i])
                answer = i
        return answer
                
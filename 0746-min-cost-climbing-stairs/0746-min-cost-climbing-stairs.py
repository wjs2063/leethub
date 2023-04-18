class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [int(1e10)]*(n + 1)
        dp[0] = 0
        dp[1] = 0
        #dp[n] := n 까지 오르는데 최소비용
        for i in range(n + 1):
            if i + 2 <= n :
                dp[i + 2] = min(dp[i + 2],dp[i] + cost[i])
            if i + 1 <= n :
                dp[i + 1] = min(dp[i + 1],dp[i] + cost[i])
            
        return dp[n]
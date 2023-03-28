class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        
        #최소한의 비용으로 모든 여행날짜를 커버 해보자 
        n = max(days)
        dp = [0]*(n + 1)
        days = set(days)
        for i in range(1,n + 1):
            if i not in days:
                dp[i] = dp[i - 1]
            else:
                dp[i] = min(dp[i - 1] + costs[0],dp[max(0,i - 7)] + costs[1],dp[max(0,i - 30)] + costs[2])
        return dp[n]
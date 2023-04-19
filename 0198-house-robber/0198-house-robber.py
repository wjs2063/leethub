class Solution:
    def rob(self, nums: List[int]) -> int:
        # i번쨰를 훔치면 i + 1 번째는 못훔친다 .
        n = len(nums)
        dp = [[0,0] for _ in range(n + 1)]
        # dp[i][0] := i번째 집을 훔치지않은경우 
        # dp[i][1] := i번째 집을 훔친경우 
        dp[0][1] = nums[0]
        for i in range(n):
            #i번째 집을 훔칠수있는경우, i - 1번째집을 훔치지않았고 i번째집을 훔치면된다
            if i >= 1:
                dp[i][1] = max(dp[i][1],dp[i - 1][0] + nums[i])
                #i번째 집을 훔치지 않는경우
                dp[i][0] = max(dp[i - 1][0],dp[i - 1][1])
        return max(dp[n - 1])
        
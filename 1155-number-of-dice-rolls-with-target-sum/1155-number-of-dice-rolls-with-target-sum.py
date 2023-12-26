class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        # 1 <=  d(t) <= k 
        # d1 + d2 + d3  ... dn = target 
        # dp[x][s] := x개 의 주사위, 1 <= dice <= k, 로 합을 s 로 만들수있는 경우의 수 
        
        dp = [[0] * (target + 1) for _ in range(n + 1)]
        # dp[i][j] := i개의 주사위로 j점수를 만들수있는 경우의수
        # dp[i + 1][j] = dp[i][j - 1] + dp[i][j - 2] ... dp[i][j - k]
        MOD = int(1e9) + 7
        # init dp 
        for i in range(1,min(target,k) + 1):
            dp[1][i] = 1
        
        for i in range(1,n + 1):
            for j  in range(1,target + 1):
                for t in range(1,k + 1):
                    if j - t >= 0 :
                        dp[i][j] = (dp[i][j] + dp[i - 1][j - t]) % MOD
        
        return dp[n][target] % MOD
            
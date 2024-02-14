class Solution:
    def numWays(self, n: int, k: int) -> int:

        """
        explanation
        
        p1,p2,p3 ... pn 
        
        즉 p(n - 2), p(n - 1), p(n) 
                              n번째 색깔이 A 색이라 가정
                              n - 1번째 색깔은 A 인경우와 A 가 아닌경우로 나뉜다.
        n - 1번째 색깔이 A 인경우는 
        n - 2번째 색깔은 A 만 아니라면 다됨 즉 (k - 1) * dp[n - 2] 가지수 
        n - 1번째 색깔이 A 가아니라면 -> k - 1가지색과 * dp[n - 1] 가지수가 가능 
        
        
        
        """
        
        dp = {}
        
        def dfs(x):
            """
            dfs(x) := x개의 post를 k가지 색으로 칠할수있는 경우 (3개이상 연속 x )
            """
            if x == 1:
                return k
            if x == 2:
                return k ** 2
            
            if x in dp:
                return dp[x]
            dp[x] = (k - 1) * (dfs(x - 1) + dfs(x - 2))
            return dp[x]

        return dfs(n)
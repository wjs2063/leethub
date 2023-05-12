class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dp = [0] * (n + 1)
        dp[n] = questions[-1][0] 
        for i in range(n - 1,0,-1):
            point,brain = questions[i - 1]
            dp[i] = point
            
            day = i + brain + 1
            
            if day <= n :
                dp[i] += dp[day]
            
            dp[i] = max(dp[i],dp[i + 1])
        return dp[1]
            
        
        
                
        
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        from collections import defaultdict
        
        points = [0] * (max(nums) + 1)
        
        for num in nums:
            points[num] += num
        dp = [0] * (max(nums) + 1)
        dp[1] = points[1]
        n = len(points)
        for i in range(2,n):
            dp[i] = max(dp[i - 2] + points[i],dp[i - 1])
        return dp[n - 1]
                
        
        
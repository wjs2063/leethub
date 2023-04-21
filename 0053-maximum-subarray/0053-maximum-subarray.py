class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # dp[i]: a0 + a1 .. ai, a1 + a2 .. ai, a2 + a3.. ai ... ai 
        # dp[i] = max(dp[i - 1] + nums[i],nums[i])
        n = len(nums)
        dp = [-int(1e10)] * n 
        dp[0] = nums[0]
        for i in range(n):
            if i >= 1:
                dp[i] = max(dp[i - 1] + nums[i],nums[i])
        return max(dp)
            
        
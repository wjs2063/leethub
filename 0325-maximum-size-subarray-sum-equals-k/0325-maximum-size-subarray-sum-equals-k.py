class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        n = len(nums)
        
        s = 0
        ans = 0
        memo = dict()
        
        for i,v in enumerate(nums):
            s += v 
            
            if s == k :
                ans = max(ans,i + 1)
            
            if s - k in memo:
                ans = max(ans,i - memo[s - k])
            
            if s not in memo:
                memo[s] = i
        return ans
            
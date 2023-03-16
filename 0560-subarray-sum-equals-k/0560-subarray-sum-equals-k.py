class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        from collections import defaultdict
        
        memo = defaultdict(int)
        n = len(nums)
        ans = 0
        s = [0]*(n)
        for i,v in enumerate(nums):
            s[i] = v
            if i >= 1:
                s[i] += s[i - 1]
            if s[i] == k:
                ans += 1
            ans += memo[s[i] - k ]
            memo[s[i]] += 1
        return ans
                
            
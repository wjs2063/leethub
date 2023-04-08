class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        
        ans = 0
        # 2 2 1 1 2 2 1 1  k = 2 
        from collections import defaultdict
        memo = defaultdict(int)
        ans = 0
        for i,v in enumerate(nums):
            nums[i] = v % 2
            if i >= 1:
                nums[i] += nums[i - 1]
            if nums[i] == k:
                ans += 1
            ans += memo[nums[i] - k]
            memo[nums[i]] += 1
        return ans
        
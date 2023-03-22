from collections import defaultdict
class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        memo = defaultdict(int)
        n = len(nums)
        ans = 0
        for i in range(n):
            if i >= 1:
                nums[i] += nums[i - 1]
            if nums[i] == goal:
                ans += 1
            ans += memo[nums[i] - goal]
            memo[nums[i]] += 1
        return ans
                
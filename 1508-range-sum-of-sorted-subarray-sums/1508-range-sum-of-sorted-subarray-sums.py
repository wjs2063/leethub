class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        ans = []
        for i,v in enumerate(nums):
            sub_sum = 0
            for j in range(i,len(nums)):
                sub_sum += nums[j]
                ans.append(sub_sum)
        
        ans.sort()
        MOD = int(1e9 + 7)
        return sum(ans[left - 1:right]) % MOD
                
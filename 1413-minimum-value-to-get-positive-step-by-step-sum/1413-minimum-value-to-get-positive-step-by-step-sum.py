class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(1,n):
            nums[i] += nums[i - 1]
        negative = []
        for v in nums:
            if v <= 0 :
                negative.append(v)
        ans = 0
        if negative:
            ans = abs(min(negative))
        return ans + 1
            
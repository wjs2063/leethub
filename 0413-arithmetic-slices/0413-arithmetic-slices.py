class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        ans = 0
        current = 0
        for idx in range(2,len(nums)):

            if nums[idx] - nums[idx - 1] == nums[idx - 1] - nums[idx - 2]:
                current += 1
                ans += current
            else:
                current = 0
        return ans

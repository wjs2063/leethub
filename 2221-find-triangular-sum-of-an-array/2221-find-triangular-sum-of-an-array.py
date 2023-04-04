class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        
        while len(nums) > 1:
            n = len(nums)
            sub = []
            for i in range(n - 1):
                sub.append((nums[i] + nums[i + 1]) % 10)
            nums = sub
        return nums[0]
                
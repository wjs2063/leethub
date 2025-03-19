class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        flip_count = 0
        for idx in range(n - 2):
            if nums[idx] == 0:
                flip_count += 1
                nums[idx] ^= 1
                nums[idx + 1] ^= 1
                nums[idx + 2] ^= 1
        if sum(nums) == n:
            return flip_count
        return -1

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        from bisect import bisect_left
        idx = bisect_left(nums,target)
        if idx < len(nums) and  nums[idx] == target:return idx
        return -1
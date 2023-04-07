class Solution:
    def minMaxGame(self, nums: List[int]) -> int:
        
        while len(nums) > 1:
            n = len(nums)
            new = [0] * (n // 2)
            for i in range(n // 2):
                if i % 2 == 0 :
                    new[i] = min(nums[2*i],nums[2*i + 1])
                else:
                    new[i] = max(nums[2*i],nums[2*i + 1])
            nums = new
        return nums[0]
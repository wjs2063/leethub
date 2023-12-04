class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i,v in enumerate(nums):
            nums[i] = [v,i]
        nums.sort()
        l,r = 0, n - 1
        
        while l < r :
            s = nums[l][0] + nums[r][0]
            
            if s == target:return [nums[l][1],nums[r][1]]
            
            if s < target:
                l += 1
            else:
                r -= 1
            
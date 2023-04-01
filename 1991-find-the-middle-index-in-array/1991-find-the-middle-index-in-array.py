class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        
        #  0 ~ left - 1,  left , left + 1 ~ 
        nums = [0] + nums
        for i in range(1,len(nums)):
            nums[i] += nums[i - 1]
        nums.append(nums[-1])
        n = len(nums)
        for i in range(1,n - 1):
            left = nums[i - 1]
            right = nums[-1] - nums[i]
            if left == right :
                return i - 1
        return -1
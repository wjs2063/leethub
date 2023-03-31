class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        # 가장큰것과 가장작은것을 짝짓는방식
        
        n = n // 2
        ans = 0
        for i in range(n):
            temp = nums[i] + nums[len(nums) - 1 - i]
            if ans < temp:
                ans = temp
        return ans
        
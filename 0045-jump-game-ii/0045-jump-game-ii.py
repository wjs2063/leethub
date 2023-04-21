class Solution:
    def jump(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)
        last = 0
        end = 0
        # we have to reach n - 1
        for i in range(n - 1):
            end = max(end,i + nums[i])
            
            if i == last:
                ans += 1
                last = end 
        return ans
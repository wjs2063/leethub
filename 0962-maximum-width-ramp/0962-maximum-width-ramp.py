class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        stack = []
        # stack 에는 오름차순만되게끔 만든다.
        s = []
        n = len(nums)
        for i,v in enumerate(nums):
            if not s or nums[s[-1]] > v:
                s.append(i)
        ans = 0
        for i in range(n - 1,-1,-1):
            while s and nums[i] >= nums[s[-1]]:
                ans = max(ans,i - s.pop())
        return ans
        
        
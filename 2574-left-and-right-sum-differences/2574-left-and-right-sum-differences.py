class Solution:
    def leftRigthDifference(self, nums: List[int]) -> List[int]:
        n = len(nums)
        l,r = 0,sum(nums)
        ans = []
        for i,v in enumerate(nums):
            r -= v 
            ans.append(abs(r - l))
            l += v
        return ans
        
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        l = nums[:]
        r = nums[:]
        
        for i in range(1,n):
            l[i] *= l[i - 1]
        
        for i in range(n - 2,-1,-1):
            r[i] *= r[i + 1]
        l = [1] + l
        r = r + [1]
        res = []
        for i in  range(1,n + 1):
            res.append(l[i - 1] * r[i])
        
            
        
        return res
            
        
        
        
class Solution:
    def leftRigthDifference(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left = nums[:]
        right = nums[:]
        for i in range(1,n):
            left[i] += left[i - 1]
        
        for i in range(n - 2,-1,-1):
            right[i] += right[i + 1]
        
        ans = []
        for i in range(n):
            if i > 0 :
                l = left[i - 1]
            else:
                l = 0
            if i < n - 1:
                r = right[i + 1]
            else:
                r = 0
            ans.append(abs(l - r))
        return ans
                
                
        
class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        
        p = [0] + nums
        n = len(p)
        for i in range(1,n):
            p[i] += p[i - 1]
        ans = []
        for i in range(1,n):
            k = i - 1
            val = nums[k] * (2*k + 2 - (n - 1) ) + p[n - 1] - 2 *p[k + 1]
            ans.append(val)
        return ans
            
        
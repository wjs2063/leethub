class Solution:
    def findLHS(self, nums: List[int]) -> int:
        from collections import Counter 
        c = Counter(nums)
        ans = 0
        for k in c :
            if k + 1 in c :
                ans = max(ans,c[k] + c[k + 1])
        return ans

            
            

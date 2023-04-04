class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos = []
        neg = []
        
        for i,v in enumerate(nums):
            if v < 0 :neg.append(v)
            else:pos.append(v)
        ans = []
        
        n = len(pos)
        for i in range(n):
            ans.append(pos[i])
            ans.append(neg[i])
        return ans
        
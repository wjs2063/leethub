class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        d = dict()
        
        for i,v in enumerate(nums):
            d[v] = i
        
        for x,y in operations:
            nums[d[x]] = y
            d[y] = d[x]
        return nums
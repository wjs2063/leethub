from heapq import heappush,heappop,heapify
class Solution:
    def maximizeGreatness(self, nums: List[int]) -> int:
        nums.sort()
        ans = 0
        for v in nums:
            if v > nums[ans]:
                ans += 1
        return ans
            
        
        
        
        
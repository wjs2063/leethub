from heapq import heappush,heappop,heapify
class Solution:
    def maximizeGreatness(self, nums: List[int]) -> int:
        nums.sort()
        sub = nums[:]
        heapify(sub)
        ans = 0
        for i,v in enumerate(nums):
            while sub and v >= sub[0]:
                heappop(sub)
            if sub and sub[0] > v:
                ans += 1
                heappop(sub)
        return ans
        
        
        
        
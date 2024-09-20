from heapq import heappush,heappop
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        h = []
        
        for i,v in enumerate(nums):
            heappush(h,-v)
        
        for _ in range(k - 1):
            heappop(h)
        return -heappop(h)
            
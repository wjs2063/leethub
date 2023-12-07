class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        from heapq import heappush,heappop,heapify
        intervals.sort(key = lambda x: x[0])
        
        
        h = []
        
        res = 0
        
        for [sn,en] in intervals:
            
            while h and h[0][0] <= sn:
                heappop(h)
            heappush(h,[en,sn])
            res = max(res,len(h))
        return res
        
            
                
        
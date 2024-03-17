class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        _max = max(x[-1] for x in intervals)
        schedule = [0] * (_max + 1)
        
        for sn,en in intervals:
            schedule[en] -= 1
            schedule[sn] += 1
        
        for i in range(1,_max +1):
            schedule[i] += schedule[i - 1]
        return max(schedule)
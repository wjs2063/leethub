from collections import deque
class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        
        grp = [[] for _ in range(n + 1)]
        
        for i,v in enumerate(manager):
            if v == -1 :continue
            grp[v].append(i)
        
        q = deque([(headID,0)])
        seen = set({headID})
        ans = 0
        while q:
            root,time = q.popleft()
            ans = max(ans,time)
            for subord in grp[root]:
                if subord in seen :continue
                seen.add(subord)
                q.append((subord,time + informTime[root]))
        return ans
from collections import deque
from collections import defaultdict
class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        
        
        bus = defaultdict(set)
        for i,v in enumerate(routes):
            for station in v:
                bus[station].add(i)
        
        
        def bfs(source,target):
            nonlocal bus
            q = deque([(source,0)])
            visit = [0]*(501)
            while q:
                station,cnt = q.popleft()
                if station == target:
                    return cnt
                for b in bus[station]:
                    if visit[b] :continue
                    visit[b] = 1
                    for x in routes[b]:
                        q.append((x,cnt + 1))
            return -1
        return bfs(source,target)
                
                
            
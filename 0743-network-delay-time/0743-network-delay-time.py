from collections import deque
from heapq import heappush,heappop
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        ans = -1
        tree = [[] for _ in range(n + 1)]    
        for x,y,z in times:
            tree[x].append([y,z])
        INF = int(1e10)
        distance = [0] + [INF]*n
        distance[k] = 0
        q = [(0,k)]
        while q:
            t,node = heappop(q)
            if distance[node] < t:continue
            for child,cost in tree[node]:
                if distance[child] > t + cost:
                    distance[child] = t + cost
                    heappush(q,(t + cost,child))
        m = max(distance)
        return m if m < INF else -1
        

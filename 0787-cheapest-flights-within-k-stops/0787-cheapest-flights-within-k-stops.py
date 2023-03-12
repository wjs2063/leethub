import heapq
from collections import defaultdict
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        grp = defaultdict(list)
        for x,y,c in flights:
            grp[x].append([y,c])
        pq = [(0,src,1)]
        INF = int(1e10)
        # 최대 n*k 개만 가능하다
        vis = [[INF]*(k + 3) for _ in range(n)]
        vis[src][1] = 0
        # vis[node][cnt] : cnt 횟수로 node를 방문할때 최소비용
        # 최대 k 번 갈아탈수있다면 그말즉 간선은 k + 1번까지 지나칠수있다는말과 동치
        while pq:
            x,node,cnt = heapq.heappop(pq)
            # 방문체크
            if node == dst:
                return x
            # 반영된이후로 다 무시
            for next_node,next_cost in grp[node]:
                if 1 <= cnt <= k + 1 and  x + next_cost < vis[next_node][cnt - 1] :
                    vis[next_node][cnt] = x + next_cost
                    heapq.heappush(pq,[x + next_cost,next_node,cnt + 1])
        return -1
                
                
                
                
            
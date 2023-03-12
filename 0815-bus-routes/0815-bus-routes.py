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
            # 버스를 방문체크한다
            visit = [0]*(501)
            while q:
                station,cnt = q.popleft()
                if station == target:
                    return cnt
                # 현재 station 에 오는 버스들을 돌면서 체크 
                for b in bus[station]:
                    # 이전에 체크했던 버스면 굳이 체크 x
                    if visit[b] :continue
                    #방문체크
                    visit[b] = 1
                    # 이버스가 갈수있는 경우 다 체크 
                    for x in routes[b]:
                        q.append((x,cnt + 1))
            return -1
        return bfs(source,target)
                
                
            
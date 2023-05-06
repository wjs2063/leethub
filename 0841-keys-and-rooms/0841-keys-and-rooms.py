from collections import deque
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        
        def bfs(rooms):
            vis = set()
            q = deque([])
            q.extend(rooms[0])
            vis.add(0)
            for x in rooms[0]:
                vis.add(x)
            while q:
                x = q.popleft()
                
                for nx in rooms[x]:
                    if nx not in vis:
                        vis.add(nx)
                        q.append(nx)
            return vis
        vis = bfs(rooms)
        for i,v in enumerate(rooms):
            if not v :continue
            if i not in vis:return False
        return True
        
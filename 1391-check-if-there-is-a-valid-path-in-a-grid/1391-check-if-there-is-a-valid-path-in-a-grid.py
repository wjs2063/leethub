class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        from collections import defaultdict,deque
        n,m = len(grid),len(grid[0])
        def in_range(x,y):
            if 0 <= x < n and 0 <= y < m :return 1
            return 0
            
        def bfs():

            d = defaultdict(list)
            d[1] = [(0,-1),(0,1)]
            d[2] = [(-1,0),(1,0)]
            d[3] = [(0,-1),(1,0)]
            d[4] = [(0,1),(1,0)]
            d[5] = [(0,-1),(-1,0)]
            d[6] = [(-1,0),(0,1)]


            seen = set()
            q = deque([(0,0)])
            seen.add((0,0))
            while q:
                x,y = q.popleft()
                if (x,y) == (n - 1,m - 1):return True
                now = grid[x][y]
                for dx,dy in d[now]:
                    nx = x + dx
                    ny = y + dy
                    if not in_range(nx,ny) or (nx,ny) in seen:continue
                    nn = grid[nx][ny]
                    if (-dx,-dy) in d[nn]:
                        seen.add((nx,ny))
                        q.append((nx,ny))
                        
            return False
        return bfs()
        
        
        
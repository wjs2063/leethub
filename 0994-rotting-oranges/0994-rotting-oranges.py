class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        from collections import deque
        n = len(grid)
        m = len(grid[0])
        rotten = 0
        fresh = 0
        for r in range(n):
            for c in range(m):
                if grid[r][c] == 1:
                    fresh +=1
                if grid[r][c] == 2:
                    rotten += 1
        def bfs(cnt):
            if fresh <= 0 :return 0
            t = rotten
            q = deque([])
            seen = set()   
            for r in range(n):
                for c in range(m):
                    if grid[r][c] == 2:
                        q.append((r,c,0))
                        seen.add((r,c))
            
            while q:
                x,y,time = q.popleft()
                if t == cnt: return time
                for nx,ny in [(x + 1,y),(x - 1,y),(x, y + 1),(x, y - 1)]:
                    if not (0 <= nx < n and 0 <= ny < m ):continue
                    if (nx,ny) in seen:continue
                    if grid[nx][ny] == 1:
                        t += 1
                        if t == cnt: return time + 1
                        seen.add((nx,ny))
                        q.append((nx,ny,time + 1))
            return -1
        return bfs(fresh + rotten)
                
                    
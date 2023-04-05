class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        from collections import deque
        n = len(grid)
        m = len(grid[0])
        vis = [[0]*m for _ in range(n)]
        def bfs(x,y):
            q = deque([(x,y)])
            vis[x][y] = 1
            while q:
                x,y = q.popleft()
                for nx,ny in [(x + 1,y),(x - 1,y),(x,y - 1),(x,y + 1)]:
                    if not (0 <= nx < n and 0 <= ny < m):continue
                    if vis[nx][ny] or grid[nx][ny] == 1:continue
                    vis[nx][ny] = 1
                    q.append((nx,ny))
            return 1
        ans = 0
        
        for i in range(n):
            if grid[i][0] == 0:
                bfs(i,0)
            if grid[i][m - 1] == 0:
                bfs(i,m - 1)
        for i in range(m):
            if grid[0][i] == 0:
                bfs(0,i)
            if grid[n - 1][i] == 0:
                bfs(n - 1,i)
        for i in range(n):
            for j in range(m):
                if vis[i][j] or grid[i][j] == 1:continue
                ans += bfs(i,j)
        return ans
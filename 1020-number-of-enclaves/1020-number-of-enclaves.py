class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        # boundary 아닌 섬을 찾아라 !! 
        from collections import deque
        
        n = len(grid)
        m = len(grid[0])
        ans = 0
        vis = [[0]*m for _ in range(n)]
        
        def bfs(x,y):
            q = deque([(x,y)])
            f = 1
            vis[x][y] = 1
            cnt = 1
            while q:
                x,y = q.popleft()
                if x in [0,n - 1] or y in [0,m - 1]:
                    f = 0
                for nx,ny in [(x + 1,y),(x - 1,y),(x,y - 1),(x,y + 1)]:
                    if not (0 <= nx < n and 0 <= ny < m) or vis[nx][ny]:continue
                    if grid[nx][ny] == 0 :continue
                    cnt +=1
                    vis[nx][ny] = 1
                    q.append((nx,ny))
            return cnt if f else 0
        for i in range(1,n - 1):
            for j in range(1,m - 1):
                if not vis[i][j] and grid[i][j] == 1:
                    ans += bfs(i,j)
        return ans
        
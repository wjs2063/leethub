class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        from collections import deque
        n = len(grid1)
        m = len(grid1[0])
        
        vis = [[0]*m for _ in range(n)]
        
        # grid2 를 bfs 로돌면서 -> 그 점들이 grid1에서도 1인지 모두 체크를 하자 아니면 0 
        
        def bfs(x,y):
            vis[x][y] = 1
            q = deque([(x,y)])
            res = grid1[x][y] == grid2[x][y]
            while q:
                x,y = q.popleft()
                
                for nx,ny in [(x + 1,y),(x - 1,y),(x,y + 1),(x, y - 1)]:
                    if not (0 <= nx < n and 0 <= ny < m) :continue
                    if vis[nx][ny] or grid2[nx][ny] != 1 :continue
                    if grid1[nx][ny] != 1:res = 0
                    vis[nx][ny] = 1
                    q.append((nx,ny))
            return res
        ans = 0
        for i in range(n):
            for j in range(m):
                if not vis[i][j] and grid2[i][j] == 1:
                    ans += bfs(i,j)
        return ans
        
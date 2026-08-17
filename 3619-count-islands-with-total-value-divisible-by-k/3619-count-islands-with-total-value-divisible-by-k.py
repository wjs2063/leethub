class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        from collections import deque 

        n = len(grid)
        m = len(grid[0])

        vis = [[0] * m for _ in range(n)]

        def bfs(pos:tuple,grid,vis):
            nonlocal k
            from collections import deque 
            x,y = pos[0],pos[1]

            q = deque([(x,y)])

            dirs = [(-1,0),(1,0),(0,-1),(0,1)]

            sums = grid[x][y]
            vis[x][y] = 1

            while q :
                a, b = q.popleft()

                for dx,dy in dirs:
                    nx = a + dx
                    ny = b + dy

                    if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] >= 1  and not vis[nx][ny]:
                        sums += grid[nx][ny]
                        vis[nx][ny] = 1
                        q.append((nx,ny))
            return 1 if sums % k == 0 else 0
        ans = 0
        for row in range(n):
            for col in range(m):
                if grid[row][col] >= 1 and not vis[row][col]:
                    ans += bfs((row,col),grid,vis)
        return ans












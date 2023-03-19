from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        def bfs():
            if grid[0][0] == 1:return - 1
            q = deque([(0,0,1)])
            vis = [[0]*n for _ in range(n)]
            vis[0][0] = 1
            while q:
                x,y,cnt = q.popleft()
                if (x,y) == (n - 1,n - 1):
                    return cnt 
                for nx,ny in [(x - 1,y - 1),(x - 1,y),(x - 1,y + 1),(x,y - 1),(x,y + 1),(x + 1,y - 1),(x + 1,y),(x + 1,y + 1)]:
                    if 0 <= nx < n and 0 <= ny < n and not vis[nx][ny] and grid[nx][ny] == 0:
                        vis[nx][ny] = 1
                        q.append((nx,ny,cnt + 1))
            return -1
        return bfs()
                        
            
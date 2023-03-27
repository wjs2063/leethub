from heapq import heappush,heappop
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        def bfs():
            n = len(grid)
            m = len(grid[0])
            h = [(grid[0][0],0,0)]
            vis = [[0]*m for _ in range(n)]
            vis[0][0] = 1
            
            while h :
                cnt,x,y = heappop(h)
                if (x,y) == (n - 1,m - 1):return cnt 
                for nx,ny in [(x + 1,y),(x,y + 1)]:
                    if not (0 <= nx < n and 0 <= ny < m) or vis[nx][ny]:continue
                    vis[nx][ny] = 1
                    heappush(h,(cnt + grid[nx][ny],nx,ny))
            return -1
        return bfs()
            
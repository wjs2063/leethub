from heapq import heappush,heappop
class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        
        def bfs():
            q = [(0,(0,0,grid[0][0]))]
            dirs = {
                1:(0,1),
                2:(0,-1),
                3:(1,0),
                4:(-1,0)
            }
            # change 여부
            vis = [[0]*m for _ in range(n)]
            while q:
                cnt,(x,y,d) = heappop(q)
                #print(cnt,x,y)
                if (x,y) == (n - 1,m - 1):return cnt
                # 현재방향
                nx,ny = x + dirs[d][0],y + dirs[d][1]
                if 0 <= nx < n and 0 <= ny < m and not vis[nx][ny]:
                    heappush(q,(cnt,(nx,ny,grid[nx][ny])))
                # check 4방향
                if not vis[x][y]:
                    for i in range(1,5):
                        if i == d:continue
                        nx,ny = x + dirs[i][0], y + dirs[i][1]
                        if 0 <= nx < n and 0 <= ny < m:
                            heappush(q,(cnt + 1,(nx,ny,grid[nx][ny])))
                    vis[x][y] = 1
            return n*m
        return bfs()
                        
                    
                
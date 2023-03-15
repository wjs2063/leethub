from collections import deque
class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        
        def bfs():
            distance = [[-1]*m for _ in range(n)]
            q = deque([(0,0,0)])
            # distance[x][y] := x,y 까지오는데 필요한 벽돌제거수
            distance[0][0] = 0
            while q:
                x,y,cnt = q.popleft()
                
                for nx,ny in [(x + 1,y),(x - 1,y),(x,y - 1),(x,y + 1)]:
                    #범위안에있고 방문하지않았으면 
                    if 0 <= nx < n and 0 <= ny < m and distance[nx][ny] == -1:
                    # 벽이라면 1개추가해주고
                        if grid[nx][ny] == 1:
                            distance[nx][ny] = cnt + 1
                            q.append((nx,ny,cnt + 1))
                        else:
                            distance[nx][ny] = cnt
                            q.appendleft((nx,ny,cnt))
            return distance[n - 1][m - 1]
        return bfs()
                            
                    
        
        
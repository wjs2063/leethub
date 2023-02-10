from collections import deque
class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        n = len(grid)
        q = deque([(i,j) for j in range(n) for i in range(n) if grid[i][j] == 1 ])
        if len(q) == 0 or len(q) == n:return -1
        # q 에 땅을 다담고 bfs 돌리자
        dx = [-1,1,0,0]
        dy = [0,0,-1,1]
        ans = 0
        while q:
            x,y = q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or nx >= n or ny < 0 or ny >= n :continue
                #방문한지점 패스
                if grid[nx][ny] : continue
                grid[nx][ny] = grid[x][y] + 1
                q.append((nx,ny))
                ans = max(ans,grid[nx][ny])
        return ans - 1
                
        
                
            
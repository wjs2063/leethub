class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        
        grid = [[-1] * n for _ in range(n)]
        
        dx = [0,1,0,-1]
        dy = [1,0,-1,0]
        d = 0
        x,y = 0,0
        cnt = 1
        while cnt <= n  ** 2 :
            grid[x][y] = cnt
            
            nx,ny = x + dx[d],y + dy[d]
            
            if not (0 <= nx < n and 0 <= ny < n):
                d = (d + 1) % 4
                nx,ny = x + dx[d],y + dy[d]
            elif grid[nx][ny] != -1:
                d = (d + 1) % 4
                nx,ny = x + dx[d],y + dy[d]
            x,y = nx,ny
            cnt += 1
        return grid
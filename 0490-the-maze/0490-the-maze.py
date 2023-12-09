class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        vis = set()
        ans = False
        
        def in_range(x,y):
            n = len(maze)
            m = len(maze[0])
            
            if 0 <= x < n and 0 <= y < m : return 1
            return 0
        
        def dfs(maze,sx,sy,ex,ey):
            nonlocal vis 
            nonlocal ans
            dx = [-1,1,0,0]
            dy = [0,0,-1,1]
            
            if ans : return 
            for i in range(4):
                # choose direction and go 
                if (sx,sy,i) in vis:continue 
                vis.add((sx,sy,i))
                x,y = sx,sy
                nx,ny = x + dx[i],y + dy[i]
                while in_range(nx,ny) and  maze[nx][ny] != 1:
                    x,y = nx,ny 
                    nx,ny = x + dx[i], y + dy[i]
                if (x,y) == (ex,ey) :
                    ans = True
                    return
                dfs(maze,x,y,ex,ey)
                    
        sx,sy = start
        ex,ey = destination
        dfs(maze,sx,sy,ex,ey)
        return ans 
        
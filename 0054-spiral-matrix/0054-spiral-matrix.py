class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n = len(matrix)
        m = len(matrix[0])
        cnt = n * m 
        vis = set()
        x,y = 0,0
        d = 0
        
        dx = [0,1,0,-1]
        dy = [1,0,-1,0]
        res = []
        while cnt :
            res.append(matrix[x][y])
            vis.add((x,y))
            nx,ny = x + dx[d],y + dy[d]
            
            if not (0 <= nx < n and 0 <= ny < m):
                d = (d + 1) % 4
                x,y = x + dx[d],y + dy[d]
            elif (nx,ny) in vis:
                d = (d + 1) % 4
                x,y = x + dx[d],y + dy[d]
            else:
                x,y = nx,ny
            cnt -= 1
        return res
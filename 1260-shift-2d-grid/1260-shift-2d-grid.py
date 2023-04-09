class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        n = len(grid)
        m = len(grid[0])
        r = k % n*m
        ans = [[0]*m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                index = (m*i + j + k) % (n * m)
                r,c = divmod(index,m)
                ans[r][c] = grid[i][j]
        return ans
        
        
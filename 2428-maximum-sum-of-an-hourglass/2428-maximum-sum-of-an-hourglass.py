class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        def in_range(x,y):
            if 0 <= x < n and 0 <= y < m :return 1
            return 0
        
        def solve(x,y):
            s = 0
            
            for nx,ny in [(x - 1,y - 1),(x - 1,y),(x - 1,y + 1),(x,y),(x + 1,y - 1),(x + 1,y),(x + 1,y + 1)]:
                if not in_range(nx,ny):return 0
                s += grid[nx][ny]
            return s 
        ans = 0
        for i in range(1,n - 1):
            for j in range(1,m - 1):
                ans = max(ans,solve(i,j))
        return ans
                
            
            
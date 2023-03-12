import heapq
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        h = [(grid[0][0],0,0)]
        seen = [[0]*n for _ in range(n)]
        seen[0][0] = 1
        ans = 0
        while h :
            t,x,y = heapq.heappop(h)
            ans = max(ans,t)
            if (x,y) == (n - 1,n - 1):
                return ans
            for nx,ny in [(x + 1,y),(x - 1,y),(x,y + 1),(x,y - 1)]:
                if 0 <= nx < n and 0 <= ny < n and not seen[nx][ny]:
                    seen[nx][ny] = 1
                    heapq.heappush(h,(grid[nx][ny],nx,ny))
        return ans
                    
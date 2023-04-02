class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        from collections import deque
        n = len(heights)
        m = len(heights[0])
        max_val = 0
        min_val = 0
        for i in range(n):
            max_val = max(max_val,max(heights[i]))
            min_val = min(min_val,min(heights[i]))
        sn,en = min_val,max_val
        def bfs(mid):
            q = deque([(0,0)])
            seen = set()
            seen.add((0,0))
            while q:
                x,y = q.popleft()
                if (x,y) == (n - 1,m - 1):return 1
                for nx,ny in [(x + 1,y),(x - 1,y),(x,y + 1),(x,y - 1)]:
                    if not (0 <= nx < n and 0 <= ny < m) or (nx,ny) in seen:continue
                    if abs(heights[x][y] - heights[nx][ny]) > mid:continue
                    seen.add((nx,ny))
                    q.append((nx,ny))
            return 0
                    
        ans = 0
        while sn <= en:
            mid = (sn + en) // 2
            
            ff = bfs(mid)
            if ff :
                ans = mid
                en = mid - 1
            else:
                sn = mid + 1
        return ans
                
            
            
        
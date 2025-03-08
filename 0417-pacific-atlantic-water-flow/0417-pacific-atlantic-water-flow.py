from collections import deque
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        pacific,atlantic = deque([]),deque([])
        row = len(heights)
        col = len(heights[0])
        for r in range(row):
            pacific.append((r,0))
            atlantic.append((r,col - 1))
        for c in range(col):
            pacific.append((0,c))
            atlantic.append((row - 1,c))
        
        def breadFirst(q):
            reachable = set()
            vis = set(list(q))
            while q:
                x,y = q.popleft()
                reachable.add((x,y))
                for nx,ny in [(x + 1,y),(x - 1,y),(x,y - 1),(x,y + 1)]:
                    if nx < 0 or nx >= row or ny < 0 or ny >= col :continue
                    if heights[x][y] > heights[nx][ny]:continue
                    if (nx,ny) in vis:continue
                    vis.add((nx,ny))
                    q.append((nx,ny))
            return reachable
        reachable_pacific = breadFirst(pacific)
        reachable_atlantic = breadFirst(atlantic)
        return list(reachable_pacific.intersection(reachable_atlantic))


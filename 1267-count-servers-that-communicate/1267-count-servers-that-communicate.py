class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        # 가로,세로
        n,m = len(grid),len(grid[0])
        row = [set() for _ in range(n)]
        col = [set() for _ in range(m)]
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    row[i].add((i,j))
                    col[j].add((i,j))
        ans = set()
        for i in range(n):
            if len(row[i]) >= 2:
                for x,y in row[i]:
                    ans.add((x,y))
        for i in range(m):
            if len(col[i]) >= 2:
                for x,y in col[i]:
                    ans.add((x,y))
        return len(ans)
            
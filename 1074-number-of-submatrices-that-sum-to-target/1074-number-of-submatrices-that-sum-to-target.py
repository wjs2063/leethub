class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        n = len(matrix)
        m = len(matrix[0])
        
        
        sub = [[0]*(m + 1) for _ in range(n + 1)]
        for i in range(n):
            for j in range(m):
                v = matrix[i][j]
                sub[i + 1][j + 1] = sub[i + 1][j] + sub[i][j + 1] - sub[i][j] + matrix[i][j]
        ans = 0
        for i in range(1,n + 1):
            for j in range(i,n + 1):
                d = defaultdict(int)
                d[0] = 1
                for k in range(1,m + 1):
                    v = sub[j][k] - sub[i - 1][k]
                    ans += d[v - target]
                    d[v] += 1
        return ans
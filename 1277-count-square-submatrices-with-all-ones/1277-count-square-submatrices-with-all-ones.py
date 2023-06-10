class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        m = len(matrix[0])
        for i in range(n):
            matrix[i] = [0] + matrix[i]
        matrix.insert(0,[0] *(m + 1))
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        for r in range(1,n + 1):
            for c in range(1,m + 1):
                if matrix[r][c] == 1:
                    dp[r][c] = 1 + min(dp[r - 1][c],dp[r][c - 1],dp[r - 1][c - 1])
        return sum(sum(dp[i]) for i in range(n + 1))
                    

        
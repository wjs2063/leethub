from collections import deque
class Solution:
    def numSquares(self, n: int) -> int:
        # perfect square  bfs solution
        """
        seen = set()
        q = deque([(0,0)])
        square = []
        for i in range(1,n + 1):
            if i**2 > n:
                break
            square.append(i**2)
        seen.add((0,0))
        while q :
            cnt,root = q.popleft()
            if root == n:return cnt
            for sq in square:
                if root + sq > n :continue
                if (cnt + 1,root + sq) in seen :continue
                seen.add((cnt + 1,root + sq))
                q.append((cnt + 1,root + sq))
        
        """
        square = []
        for i in range(1,n + 1):
            if i**2 > n:
                break
            square.append(i**2)
        """
        dp solution
        
        """
        # dp[i] := i를 square 합으로 만드는데 최소
        INF = int(1e10)
        dp = [INF]*(n + 1)
        dp[0] = 0
        for i in range(1,n + 1):
            for s in square:
                if i - s >= 0:
                    dp[i] = min(dp[i],dp[i - s] + 1)
        return dp[n]
            
        
from collections import deque
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        
        def bfs(amount):
            q = deque([(0,0)])
            visited = [0]*(amount + 1)
            while q:
                x,cnt = q.popleft()
                if x == amount :
                    return cnt 
                for coin in coins:
                    nx = x + coin
                    if nx > amount or visited[nx] :continue
                    visited[nx] = 1
                    q.append((nx,cnt + 1))
            return -1
        return bfs(amount)
                    
        
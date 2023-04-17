class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        from collections import deque
        def bfs(x):
            q = deque([(x,0)])
            seen = set()
            seen.add(x)
            while q:
                x,cnt = q.popleft()
                if x == 1:return cnt
                if x % 2 == 0 and x // 2 not in seen:
                    q.append((x//2,cnt + 1))
                    seen.add(x//2)
                elif x % 2 and 3 * x + 1 not in seen:
                    q.append((3 * x + 1,cnt + 1))
                    seen.add(3 * x + 1)
            return 0
        ans = []
        for num in range(lo,hi + 1):
            ans.append([num,bfs(num)])
        ans.sort(key = lambda x:(x[1],x[0]))
        sub = []
        for x,y in ans:
            sub.append(x)
        return sub[k - 1]
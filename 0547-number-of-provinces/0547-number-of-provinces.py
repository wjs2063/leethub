class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        seen = set()
        from collections import deque,defaultdict
        grp = defaultdict(list)
        n = len(isConnected)
        for i in range(n):
            for j in range(n):
                if isConnected[i][j]:
                    grp[i].append(j)
                    grp[j].append(i)
        def bfs(i):
            q = deque([i])
            
            while q:
                root = q.popleft()
                for node in grp[root]:
                    if node in seen:continue
                    seen.add(node)
                    q.append(node)
            return 1
        ans = 0
        for i in range(n):
            if i in seen:continue
            ans += bfs(i)
        return ans
                
        
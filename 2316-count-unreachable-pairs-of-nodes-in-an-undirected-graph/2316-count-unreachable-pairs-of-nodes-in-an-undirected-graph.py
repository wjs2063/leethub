from collections import defaultdict,deque
class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        vis = [0]*n
        graph = [[] for _ in range(n)]
        for sn,en in edges:
            graph[sn].append(en)
            graph[en].append(sn)
        memo = defaultdict(int)
        def bfs(i):
            nonlocal vis
            q = deque([i])
            vis[i] = 1
            cnt = 1
            while q :
                x = q.popleft()
                for adj in graph[x]:
                    if vis[adj] : continue
                    cnt += 1
                    vis[adj] = 1
                    q.append(adj)
            return cnt
        ans = []
        for i in range(n):
            if vis[i] : continue
            ans.append(bfs(i))
        answer = 0
        answer = n*(n - 1) // 2
        print(ans)
        for v in ans:
            if v <= 1: continue
            answer -= v*(v - 1) // 2
        return answer
        # memo[x] : x 번쨰 정점이 속한 연결그래프의 정점 수 
        
                
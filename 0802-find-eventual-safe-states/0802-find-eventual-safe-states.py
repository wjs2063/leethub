class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        from collections import deque,defaultdict
        
        grp = defaultdict(set)
        n = len(graph)
        
        indegree = [0]*n
        for i,v in enumerate(graph):
            for x in v:
                grp[x].add(i)
                indegree[i] += 1
        q = deque([])
        for i in range(n):
            if indegree[i] == 0:
                q.append(i)
        ans = []
        while q:
            x = q.popleft()
            ans.append(x)
            for nn in grp[x]:
                indegree[nn] -= 1
                if indegree[nn] == 0:
                    q.append(nn)
        return sorted(ans)
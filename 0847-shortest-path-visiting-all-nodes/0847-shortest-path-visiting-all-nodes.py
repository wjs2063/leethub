class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        from collections import deque
        n = len(graph)
        end = (1 << n) - 1
        
        q = deque([(node,1 << node,0) for node in range(n)])
        seen = set()
        for node in range(n):
            seen.add((node,1 << node))
        while q:
            root,MASK,cnt = q.popleft()
            if MASK == end:return cnt
            for nn in graph[root]:
                if (nn,MASK | (1 << nn)) in seen:continue
                seen.add((nn,MASK | (1 << nn)))
                q.append((nn,MASK | (1 << nn),cnt + 1))
        return -1
            
            
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        from collections import deque
        n = len(graph)
        color = [-1]*(n + 1)
        def bfs(i):
            q = deque([i])
            color[i] = 0

            while q:
                node = q.popleft()
                for adj in graph[node]:
                    if color[node] == color[adj] :return False
                    if color[adj] != -1:continue 
                    if color[adj] == - 1:
                        color[adj] = 1 - color[node]
                        q.append(adj)
            return True
        flag = True
        for i in range(n):
            if color[i] == -1:
                flag = bfs(i)
                if not flag:return flag
        return flag
                    
                    
                
        
        
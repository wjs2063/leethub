class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:
        
        from collections import deque 
        
        n = len(edges)
        graph = [set() for _ in range(n + 1)]
        
        for _,(a,b) in enumerate(edges):
            graph[a].add(b)
            graph[b].add(a)
        
        def bfs(start):
            q = deque([start])
            vis = [0] * (n + 1)
            vis[start] = 1
            dist = -1
            last_node = -1
            while q: 
                next_queue = deque([])
                while q:
                    vertex = q.popleft()
                    for adj_vertex in graph[vertex]:
                        if vis[adj_vertex] : continue
                        vis[adj_vertex] = 1
                        next_queue.append(adj_vertex)

                dist += 1
                q = next_queue
                last_node = vertex
            return dist,last_node
        farthest_dist,farthest_node = bfs(0)
        dist,node = bfs(farthest_node)
        return dist
            
                
                
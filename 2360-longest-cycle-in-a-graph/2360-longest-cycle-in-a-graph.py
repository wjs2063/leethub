from collections import defaultdict
class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        graph = defaultdict(list)
        n = len(edges)
        for i,v in enumerate(edges):
            graph[i].append(v)
        vis = [0]*(n + 1)
        
        def dfs(i):
            stack = [(i,0)]
            path = dict()
            # path[x] -> x 번째 노드를 방문한 순서 
            vis[i] = 1
            while stack:
                x,i = stack.pop()
                vis[x] = 1
                path[x] = i
                if not graph[x] :return -1
                next_node = graph[x][0]
                if vis[next_node] :
                    if next_node in path:
                        return i - path[next_node] + 1
                    return -1
                stack.append((next_node,i + 1))
            return -1
        ans = -1
        for i in range(n):
            if vis[i] : continue
            temp = dfs(i)
            ans = max(ans,temp)
        return ans
        
                
        
        
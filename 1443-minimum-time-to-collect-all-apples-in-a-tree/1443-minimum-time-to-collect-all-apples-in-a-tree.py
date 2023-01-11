from collections import defaultdict
class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        # root 에서 가장가까운 2 번 들리고 2번에서 남은 4,5 에서 bfs 로 찾자
        graph = defaultdict(list)
        # 그래프추가
        for v1,v2 in edges:
            graph[v1].append(v2)
            graph[v2].append(v1)
        # dfs 의미 : 현재 node, parent: node 의 부모 -> 사과를 수집하고 node 까지 돌아오는데 걸리는시간
        def dfs(node,parent):
            nonlocal hasApple
            ret = 0
            
            for adj in graph[node]:
                # 부모노드로는 못가게 막아보자
                if adj != parent:
                    ret += dfs(adj,node)
            # 현재노드에 사과가있어?
            if ret or hasApple[node]:
                return ret + 2
            return ret
        # 루트노트 1개만있을때 그리고 거기에 사과만있을때를 생각해보자
        x = dfs(0,-1) - 2
        return x if x > 0 else 0
                
        
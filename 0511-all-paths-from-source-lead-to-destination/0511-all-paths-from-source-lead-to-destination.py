class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        # graph[a] = [...] -> a 에서 나가는 노드 
        # s -> d 로 가는 적어도 1개이상의 패스 존재 
        # 노드에서 노드(나가는노드없는) 거면 그게 도착점임 
        # s -> d 로가는 패스는 유한함 

        # 즉 모든 길이 d로 통하는 패스 찾기 
        from collections import defaultdict
        graph = defaultdict(list)
        for a,b in edges:
            graph[a].append(b)
        if len(graph[destination]) != 0 :return False
        vis = [0] * n # 방문 x 0, 탐색중 1 , 탐색완료 2 
        def dfs(node:int,destination:int):
            if len(graph[node]) == 0 and node != destination:return False 
            nonlocal vis 
            # 탐색중 
            vis[node] = 1
            for next_node in graph[node]:
                # 사이클인경우 False
                if vis[next_node] == 2 :continue 
                if vis[next_node] == 1:return False
                # node -> destination 못가는경우 False 
                if not dfs(next_node,destination):return False
            # 방문 표시  
            vis[node] = 2
            return True
        return dfs(source,destination)

                
            




        
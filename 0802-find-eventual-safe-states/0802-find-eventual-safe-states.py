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
        # 해결 키포인트 
        # terminal 노드에서 시작해서 차수를 빼가면서 진행한다 -> 방향그래프이기때문에 
        # 다음 노드에서 간선 하나 제거했을때 차수가 0이면 유일한 통로라는 의미이므로 다음 q에 추가한다
        while q:
            x = q.popleft()
            ans.append(x)
            for nn in grp[x]:
                indegree[nn] -= 1
                if indegree[nn] == 0:
                    q.append(nn)
        return sorted(ans)
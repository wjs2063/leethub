class Solution:
    def findOrder(self, n: int, pre: List[List[int]]) -> List[int]:
        from collections import deque
        
        grp = [[] for _ in range(n)]
        
        for x,y in pre:
            grp[y].append(x)
        
        def topologicalsort():
            indegree = [0]*n
            for x,y in pre :
                indegree[x] += 1
            q = deque([])
            seen = [0]*n
            for i,v in enumerate(indegree):
                if v == 0: 
                    q.append(i)
            ans = []
            while q:
                r = q.popleft()
                ans.append(r)
                for nn in grp[r]:
                    indegree[nn] -= 1
                    if indegree[nn] == 0:
                        q.append(nn)
            return ans
        ans = topologicalsort()
        return ans if len(ans) == n else []
                
                
            
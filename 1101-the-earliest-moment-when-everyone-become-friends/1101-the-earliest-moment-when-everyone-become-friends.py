class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        
        def find(parent,a):
            if parent[a] != a:
                parent[a] = find(parent,parent[a])
            return parent[a]
        
        def union(parent,a,b):
            x = find(parent,a)
            y = find(parent,b)
            parent[x] = y 
        parent = [i for i in range(n)]
        logs.sort(key = lambda x: x[0])
        
        res = -1 
        
        for [time,pa,pb] in logs:
            if find(parent,pa) == find(parent,pb):continue
            union(parent,pa,pb)
            
            res = max(res,time)
        # check every person is be friend 
        x = find(parent,0)
        for i in range(n):
            if x == find(parent,i):continue
            return -1
        return res
            
        
        
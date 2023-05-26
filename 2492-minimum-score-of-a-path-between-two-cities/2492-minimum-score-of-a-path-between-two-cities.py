class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        roads.sort(key = lambda x:x[2])
        
        def find(a):
            if parent[a] != a :
                parent[a] = find(parent[a])
            return parent[a]
    
        def union(a,b):
            x = find(a)
            y = find(b)
            parent[x] = y
        
        
        parent = [i for i in range(n + 1)]
        res = int(1e10)
        for x,y,cost in roads:
            union(x,y)
        for x,y,cost in roads:
            if find(1) == find(x) == find(y):
                res = min(res,cost)
            
        return res
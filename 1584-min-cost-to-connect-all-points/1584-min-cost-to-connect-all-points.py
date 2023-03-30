class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        # MST 
        # 모든 점과의 거리 다 계산
        parent = [i for i in range(n)]
        def find(a):
            if parent[a] != a:
                parent[a] = find(parent[a])
            return parent[a]
        def union(a,b):
            a,b = find(a),find(b)
            parent[a] = b
        edges = []
        for i in range(n):
            for j in range(i + 1,n):
                x,y = points[i]
                z,w = points[j]
                dist = abs(x - z) + abs(y - w)
                edges.append((dist,i,j))
        edges.sort()
        ans = 0
        for d,x,y in edges:
            if find(x) != find(y):
                union(x,y)
                ans += d
        return ans
                
                
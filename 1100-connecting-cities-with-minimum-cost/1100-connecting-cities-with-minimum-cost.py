class Solution:
    def minimumCost(self, n: int, connections: List[List[int]]) -> int:
        
        def find_parent(parent,x):
            if parent[x] != x:
                parent[x] = find_parent(parent,parent[x])
            return parent[x]
        
        def union(parent,x,y):
            a = find_parent(parent,x)
            b = find_parent(parent,y)
            parent[a] = b
        connections.sort(key=lambda x:x[-1])
        cost = 0 
        parent = [i for i in range(n + 1)]
        for x,y,connection_cost in connections:
            if find_parent(parent,x) == find_parent(parent,y):continue
            union(parent,x,y)
            cost += connection_cost
        # check all nodes is connected 
        node_set = set()
        for x in range(1,n + 1):
            node_set.add(find_parent(parent,x))
        return cost if len(node_set) == 1 else -1

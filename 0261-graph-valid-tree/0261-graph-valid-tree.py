from collections import defaultdict,deque
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        tree = defaultdict(list)
        
        for a,b in edges:
            tree[a].append(b)
            tree[b].append(a)
        # check there is no cycle in graph
        
        def find_parent(parent,a):
            if parent[a] != a :
                parent[a] = find_parent(parent,parent[a])
            return parent[a]
        
        def union(parent,a,b):
            x = find_parent(parent,a)
            y = find_parent(parent,b)
            parent[x] = y 
#         def bfs(node,n):
#             q = deque([node])
#             parent = [i for i in range(n)]
#             vis = {node}
            
#             while q :
#                 x = q.popleft()
#                 for child in tree[x]:
#                     if child in vis:continue
#                     if find_parent(parent,x) == find_parent(parent,child):return False 
#                     union(parent,x,child)
#                     vis.add(child)
#                     q.append(child)
#             return True
        parent = [i for i in range(n)]
        for a,b in edges:
            if find_parent(parent,a) == find_parent(parent,b):return False
            union(parent,a,b)
        for i in range(n):
            find_parent(parent,i)
        return True if len(set(parent)) == 1 else False
            
            
            
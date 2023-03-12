from collections import defaultdict
class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        # 필요한것 , 각 노드 i의 서브트리의 총 노드 개수 
        tree = defaultdict(list)
        for x,y in edges:
            tree[x].append(y)
            tree[y].append(x)
        
        sub_node = [1]*n
        weight_sum = [0]*n
        
        def dfs(root,parent):
            for child in tree[root]:
                if child == parent:continue
                dfs(child,root)
                sub_node[root] += sub_node[child]
                weight_sum[root] += weight_sum[child] + sub_node[child]

        def dfs1(root,parent):
            for child in tree[root]:
                if child == parent:continue
                weight_sum[child] = weight_sum[root] - sub_node[child] + n - sub_node[child]
                dfs1(child,root)
        dfs(0,-1)
        dfs1(0,-1)
        return weight_sum

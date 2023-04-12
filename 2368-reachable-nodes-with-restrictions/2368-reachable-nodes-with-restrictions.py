class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        from collections import defaultdict
        restricted = set(restricted)
        tree_node = defaultdict(list)
        for n1,n2 in edges:
            tree_node[n1].append(n2)
            tree_node[n2].append(n1)
        seen = set()
        ans = 0
        def dfs(node):
            nonlocal ans
            seen.add(node)
            ans += 1
            
            for next_node in tree_node[node]:
                if next_node in seen or next_node in restricted:continue
                dfs(next_node)
        dfs(0)
        return ans
            
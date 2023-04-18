class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        from collections import defaultdict
        graph = defaultdict(list)
        for parent,child in edges:
            graph[child].append(parent)
        # root 의 서브트리를 모드 반환해서 넘기자
        
        def dfs(root):
            if not graph[root]: return []
            sub = []
            for child in graph[root]:
                if child in seen:continue
                sub.append(child)
                seen.add(child)
                sub.extend(dfs(child))
            return sub
        ans = [[] for _ in range(n)]
        for i in range(n):
            seen = set()
            ans[i].extend(sorted(dfs(i)))
        return ans
            
            
                
            
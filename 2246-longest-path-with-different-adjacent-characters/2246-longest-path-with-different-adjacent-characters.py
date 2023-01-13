from collections import defaultdict
class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        
        
        graph = defaultdict(list)
        for i,v in enumerate(parent):
            graph[v].append(i)
        
        answer = 1
        def dfs(vertex):
            nonlocal s
            nonlocal answer
            nonlocal graph
            if vertex not in graph:
                return 1
            res = 1
            for child in graph[vertex]:
                ret = dfs(child)
                if s[vertex] != s[child]:
                    answer = max(answer,res + ret)
                    res = max(res,ret + 1)
            return res
        dfs(0)
        return answer
                
                
            
        
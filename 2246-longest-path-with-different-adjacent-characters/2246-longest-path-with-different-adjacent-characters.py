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
                    # 
                    answer = max(answer,res + ret)
                    # 자기자신 알파벳 더해서, 길이 비교해서 max 값 (이유는 제일 긴 길이 찾아주기위해서)( child 중1개만 선택해야하는상황)
                    res = max(res,ret + 1)
            return res
        dfs(0)
        return answer
                
                
            
        
class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        t={}
        for i in range(1,len(parent)):
            if parent[i] not in t:
                t[parent[i]]=[i]
            else:
                t[parent[i]].append(i)
            
        answer = 1
        def dfs(vertex):
            nonlocal s
            nonlocal answer
            if vertex not in t:
                return 1
            res = 1
            for child in t[vertex]:
                ret = dfs(child)
                if s[vertex] != s[child]:
                    answer = max(answer,res + ret)
                    res = max(res,ret + 1)
            return res
        dfs(0)
        return answer
                
                
            
        
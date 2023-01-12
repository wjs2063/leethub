from collections import defaultdict
class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        graph = defaultdict(list)
        for e1,e2 in edges:
            graph[e1].append(e2)
            graph[e2].append(e1)
        # graph[x]  := x와 인접한 vertex 
    
        answer = [0]*(n)
        def dfs(vertex: int,labels,parent) -> dict:
            nonlocal answer
            ret = defaultdict(int)
            # add := current node
            ret[labels[vertex]] += 1
            # dfs 돌면서 자신의 서브트리들의 알파벳 개수를 구해온다
            for child in graph[vertex]:
                if child == parent:continue
                x = dfs(child,labels,vertex)
                for k in x:
                    ret[k] += x[k]
            answer[vertex] = ret[labels[vertex]]
            return ret
        dfs(0,labels,-1)
        return answer
            
        
            
            
            
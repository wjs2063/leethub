class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        
        from collections import defaultdict
        
        grp = defaultdict(list)
        
        for i,v in enumerate(pid):
            p = ppid[i]
            grp[p].append(v)
        vis = set()
        ans = []
        def dfs(root): 
            nonlocal vis,ans 
            vis.add(root)
            ans.append(root)
            for child in grp[root]:
                if child in vis:continue
                dfs(child)
        dfs(kill)
        
        return ans
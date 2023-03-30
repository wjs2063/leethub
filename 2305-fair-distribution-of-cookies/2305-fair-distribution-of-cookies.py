class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        # k 명한테 나누어주어야하는데 
        n = len(cookies)
        info = [0]*(k)
        ans = int(1e10)
        
        def dfs(info,idx):
            nonlocal ans
            if idx == n:
                ans = min(ans,max(info))
                return

            for j in range(k):
                if info[j] + cookies[idx] < ans :
                    info[j] += cookies[idx]
                    dfs(info,idx + 1)
                    info[j] -= cookies[idx]
        dfs(info,0)
        return ans
        
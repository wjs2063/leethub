class Solution:
    def printVertically(self, s: str) -> List[str]:
        s = list(map(list,s.split()))
        m = 0
        for item in s :
            m = max(m,len(item))
        for i,v in enumerate(s):
            s[i] += " " * (m - len(v))
        ans = []
        for i in range(m):
            sub = ""
            for idx,v in enumerate(s):
                sub += v[i]
            sub = sub.rstrip()
            ans.append(sub)
        return ans
            
        
    
            
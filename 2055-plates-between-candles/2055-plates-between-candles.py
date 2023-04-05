class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        # initialize 
        left = [n]*n
        right = [-1]*n
        for i,v in enumerate(s):
            if v == "|":
                left[i] = i
            elif i >= 1:
                left[i] = left[i - 1]
        for i in range(n - 1,-1,-1):
            if s[i] == "|":
                right[i] = i
            elif i <= n - 2:
                right[i] = right[i + 1]
        p = [0]*(n + 1)
        for i,v in enumerate(s):
            if v == "*":
                p[i + 1] = 1
            p[i + 1] += p[i]
        print(left)
        print(right)
        print(p)
        ans = []
        for sn,en in queries:
            r,l = left[en],right[sn]
            if sn <= l < r <= en:
                ans.append(p[r + 1] - p[l])
            else:
                ans.append(0)
        return ans
                
            
            
            
        
        
        
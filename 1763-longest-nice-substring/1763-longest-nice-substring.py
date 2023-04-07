class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        from collections import Counter
        n = len(s)
        
        for length in range(n,0,-1):
            for i in range(n - length + 1):
                c = Counter(s[i:i + length])
                f = 1
                for k in c:
                    if c[k.lower()] * c[k.upper()] == 0:
                        f = 0
                        break
                if f:
                    return s[i:i + length]
        return ""
                        
                
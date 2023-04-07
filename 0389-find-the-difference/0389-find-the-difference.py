class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s = list(s)
        t = list(t)
        s.sort()
        t.sort()
        for i,v in enumerate(s):
            if v == t[i]:continue
            return t[i]
        return t[-1]
        
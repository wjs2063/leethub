class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        
        ns = len(s)
        nt = len(t)
        # always ns <= nt 
        if ns > nt :
            return self.isOneEditDistance(t,s)
        if nt - ns > 1 :
            return False
        if ns == nt :
            # all same 
            if s == t  :
                return False
            # difference_cnt > 1
            d = -1
            for i in range(nt):
                if s[i] != t[i]:
                    d = i 
                    break 
            return s[:d] == t[:d] and s[d + 1:] == t[d + 1:]
        if ns and  nt - ns == 1 :
            # only one is diffrent
            diff_cnt = 0
            d = -1
            for i in range(ns):
                if s[i] != t[i]:
                    d = i
                    diff_cnt += 1
                    break 
            if diff_cnt == 0 :
                return True
            if diff_cnt == 1 :
                return s[d:] == t[d + 1:]
        return nt == ns + 1
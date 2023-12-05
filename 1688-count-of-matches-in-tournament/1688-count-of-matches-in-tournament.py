class Solution:
    def numberOfMatches(self, n: int) -> int:
        
        res = 0
        
        while n > 1:
            a,b = divmod(n,2)
            if b :
                res += a + 1
            else:
                res += a
            n = a
        return res
        
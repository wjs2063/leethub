class Solution:
    def totalMoney(self, n: int) -> int:
        p = [1,2,3,4,5,6,7]
        s = 28
        q,r = divmod(n,7)
        # n-1 th week -> full -> 
        # n-th week 
        return sum([7*i for i in range(q)]) + s * q + q * (r) + sum(p[:r])
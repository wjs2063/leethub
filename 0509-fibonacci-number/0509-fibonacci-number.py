class Solution:
    def fib(self, n: int) -> int:
        a,b = 0,1
        if n <= 1 : return n 
        for _ in range(2,n + 1):
            a,b = b, a + b
        return b
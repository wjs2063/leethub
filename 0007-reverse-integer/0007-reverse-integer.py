class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            x = str(x)
            t = int(str("-") + x[1:][::-1])
            return t if -(2**31) <= t <= 2**31 - 1 else 0
        x = str(x)
        t = int(x[::-1])
        return t if t <= 2**31 - 1 else 0 
        
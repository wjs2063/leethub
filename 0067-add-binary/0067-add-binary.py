class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = int("0b" + a,2)
        b = int("0b" + b,2)
        return bin(a + b)[2:]
        
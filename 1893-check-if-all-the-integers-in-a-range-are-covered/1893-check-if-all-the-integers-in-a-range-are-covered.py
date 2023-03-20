class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        p = [0]*(50 + 2)
        for s,e in ranges:
            p[s] += 1
            p[e + 1] -= 1
        for i in range(1,51):
            p[i] += p[i - 1]
        for i in range(left,right + 1):
            if p[i] <= 0:return False
        return True
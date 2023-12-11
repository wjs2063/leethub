class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        n = len(arr)
        from collections import defaultdict
        c = defaultdict(int)
        
        for i,v in enumerate(arr):
            c[v] += 1
            if c[v] / n * 100 > 25:
                return v
        return -1
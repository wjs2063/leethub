class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        n = length
        
        diff = [0] * (n + 1)
        
        for sx,ex,term in updates:
            diff[sx] += term
            diff[ex + 1] -= term
        
        for i in range(1,n + 1):
            diff[i] += diff[i - 1]
        return diff[:-1]
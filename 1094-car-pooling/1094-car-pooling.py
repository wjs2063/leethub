class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        d = [0]*(1002)
        
        
        for n,s,e in trips:
            d[e] -= n
            d[s] += n
        
        for i in range(1,1002):
            d[i] += d[i - 1]
        return max(d) <= capacity
            
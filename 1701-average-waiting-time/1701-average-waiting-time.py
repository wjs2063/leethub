class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        
        en = -1
        ans = 0
        n = len(customers)
        for sn,time in customers:
            
            if en < sn :
                en = sn 
            en += time 
            ans += en - sn
        return ans / n
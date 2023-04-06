class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        
        
        d,r = numBottles,0
        ans = 0
        
        while d :
            ans += d 
            r += d 
            
            d,r = divmod(r,numExchange)
        return ans
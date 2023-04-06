class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        
        
        d,r = numBottles,0
        ans = 0
        
        while d :
            #정답갱신
            ans += d 
            #빈병 추가
            r += d 
            # 빈병을 바꾸자
            d,r = divmod(r,numExchange)
        return ans
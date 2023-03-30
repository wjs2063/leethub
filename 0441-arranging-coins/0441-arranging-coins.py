class Solution:
    def arrangeCoins(self, n: int) -> int:
        
        sn,en = 0,n
        ans = 0
        while sn <= en:
            mid = (sn + en) // 2
            # mid 까지 complete 하다
            
            if (mid*(mid + 1)) // 2 <= n:
                ans = mid
                sn = mid + 1
            else:
                en = mid - 1
        return ans 
                
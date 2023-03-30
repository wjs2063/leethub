class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        
        
        sn,en = 1,2**16
        
        while sn <= en:
            mid = (sn + en) // 2
            
            
            if mid **2 == num:
                return True
            
            if mid**2 > num:
                en = mid - 1
            elif mid ** 2 < num:
                sn = mid + 1
        return False
                
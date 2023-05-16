class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        sn,en = 1,sum(weights)
        ans = 1
        while sn <= en :
            mid = (sn + en) // 2
            # maximum weights
            cnt = 1
            w = 0 
            for i,weight in enumerate(weights):
                if weight > mid:
                    cnt = int(1e10)
                    break
                if w + weight <= mid:
                    w += weight
                else:
                    cnt += 1
                    w = weight
            if cnt > days:
                sn = mid + 1
            else:
                ans = mid
                en = mid - 1
        return ans
                    
                
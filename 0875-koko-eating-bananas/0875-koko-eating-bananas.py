class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        
        sn,en = 1,sum(piles)
        ans = 0
        while sn <= en:
            mid = (sn + en) // 2
            
            # mid 의 속도로 h 시간안에 다먹을수있냐?
            # sub_ans := mid의 속도로 모든 바나나를 다먹을수있는 시간
            sub_ans = 0
            for i,v in enumerate(piles):
                sub_ans += (v - 1) // mid + 1
            if sub_ans <= h :
                ans = mid
                en = mid - 1
            else:
                sn = mid + 1
        return ans
            
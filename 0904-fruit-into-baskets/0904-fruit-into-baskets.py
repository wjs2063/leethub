from collections import defaultdict
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        ff = defaultdict(int)
        pick = set()
        r = 0
        # l <= x < r 
        n = len(fruits)
        cnt = 0
        ans = 0
        for i,v in enumerate(fruits):
            while r < n :
                x = fruits[r]
                # 들어가있으면 계속 추가
                if x in pick:
                    ff[x] += 1
                    cnt += 1
                    r += 1
                elif x not in pick and len(pick) < 2:
                    ff[x] += 1
                    pick.add(x)
                    r += 1
                    cnt += 1
                else:
                    break
                    
            ans = max(ans,cnt)
            # 마지막에는 항상 왼쪽 제거
            ff[v] -= 1
            cnt -= 1
            if ff[v] == 0:
                pick.discard(v)
        return ans
                
            
            
            
            
            
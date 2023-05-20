class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal): return False
        # 같은경우라면 중복문자가 발생해야겠지
        if s == goal and len(s) - len(set(goal)) >= 1:return True 
        # 문자가 다른경우라면 딱 한문자만 달라야함 
        cnt = 0
        seen = set()
        for x,y in zip(s,goal):
            
            if x != y:
                if (x,y) in seen:return False
                seen.add((x,y))
        if len(seen) == 2 :
            x,y = list(seen)[0]
            if (y,x) in seen:return True
        return False
            
        
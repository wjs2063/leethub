from collections import deque,defaultdict
class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        ans = 0
        effect = defaultdict(set)
        # (x,y) 의 개수 
        ct = defaultdict(int)
        # x,y,r 을 중심으로 영향을 미칠수있는 지점들 기록 (연쇄반응)
        for x,y,r in bombs:
            ct[(x,y)] += 1
            for a,b,c in bombs:
                if (x,y) == (a,b):continue
                if (x - a)**2 +(y - b)**2 <= r**2:
                    effect[(x,y)].add((a,b,c))
        # bfs 수행
        def bfs(x,y,r):
            q = deque([(x,y,r)])
            seen = set()
            seen.add((x,y))
            res = ct[(x,y)]
            while q:
                x,y,r = q.popleft()
                for a,b,c in effect[(x,y)]:
                    if (a,b) in seen:continue
                    seen.add((a,b))
                    # 중복되어있는것들은 이전에 계산한 카운트로 더해줌
                    res += ct[(x,y)]
                    q.append((a,b,c))
            return res
        for x,y,r in bombs:
            ans = max(ans,bfs(x,y,r))
        return ans
                    
                
                    
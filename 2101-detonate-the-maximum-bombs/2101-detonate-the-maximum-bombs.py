from collections import deque,defaultdict
class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        ans = 0
        effect = defaultdict(set)
        ct = defaultdict(int)
        for x,y,r in bombs:
            ct[(x,y)] += 1
            for a,b,c in bombs:
                if (x,y) == (a,b):continue
                if (x - a)**2 +(y - b)**2 <= r**2:
                    effect[(x,y)].add((a,b,c))
        
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
                    res += ct[(x,y)]
                    q.append((a,b,c))
            return res
        for x,y,r in bombs:
            ans = max(ans,bfs(x,y,r))
        return ans
                    
                
                    
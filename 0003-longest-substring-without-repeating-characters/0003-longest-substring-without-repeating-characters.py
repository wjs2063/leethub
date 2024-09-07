from collections import defaultdict,deque
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        repeated = defaultdict(int)
        q = deque([])
        ans = 0
        for i,v in enumerate(s):
            q.append(v)
            repeated[v] += 1
            
            while repeated[v] > 1 :
                x = q.popleft()
                repeated[x] -= 1
            ans = max(ans,len(q))
        return ans
            
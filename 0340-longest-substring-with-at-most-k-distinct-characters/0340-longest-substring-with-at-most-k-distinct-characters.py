class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        from collections import deque,defaultdict
        alphabet_count = defaultdict(int)
        q = deque([])
        ans = 0
        for i,v in enumerate(s):
            alphabet_count[v] += 1
            q.append(v)
            if len(alphabet_count) > k :
                x = q.popleft()
                alphabet_count[x] -= 1
                if alphabet_count[x] == 0 :
                    alphabet_count.pop(x)
            ans = max(ans,len(q))
        return ans 


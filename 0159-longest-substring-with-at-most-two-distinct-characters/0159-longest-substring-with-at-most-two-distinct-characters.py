from collections import defaultdict
class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        memo = defaultdict(int)
        
        ans = 0 
        sn = 0
        for i,v in enumerate(s):
            
            memo[v] += 1
            
            while len(memo) > 2 :
                memo[s[sn]] -= 1
                if memo[s[sn]] == 0:
                    memo.pop(s[sn])
                sn += 1
            ans = max(ans,i - sn + 1)
        return ans
        
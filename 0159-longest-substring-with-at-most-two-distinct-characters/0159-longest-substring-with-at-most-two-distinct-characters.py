class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        from collections import defaultdict
        
        temp = 0
        ans = 0
        l,r = 0,0
        n = len(s)
        memo = defaultdict(int)
        while r < n:
            
            if len(memo) >= 2:
                if s[r] in memo:
                    memo[s[r]] += 1
                    r += 1
                    temp += 1
                else:
                    memo[s[l]] -= 1
                    if memo[s[l]] == 0:
                        del memo[s[l]]
                    l += 1
                    temp -= 1
            else:
                memo[s[r]] += 1
                r += 1
                temp += 1
            ans = max(ans,temp)
        return ans
class Solution:
    def balancedStringSplit(self, s: str) -> int:
        n = len(s)
        l,r = 0,0
        ans = 0
        for i,v in enumerate(s):
            if v == "L":
                l += 1
            else:
                r += 1
            if l and r and l == r:
                ans += 1
                l,r = 0,0
        return ans
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        from collections import Counter
        s = set(jewels)
        cc = Counter(stones)
        ans = 0
        for k in s:
            ans += cc[k]
        return ans
        
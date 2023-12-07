class Solution:
    def largestOddNumber(self, num: str) -> str:
        n = len(num)
        ans = 0
        s = ""
        for i,v in enumerate(num):
            s += v
            if int(v) % 2 == 1:
                ans = s
        return ans if ans != 0 else ""
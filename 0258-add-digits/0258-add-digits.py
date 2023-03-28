class Solution:
    def addDigits(self, num: int) -> int:
        num = str(num)
        while len(num) > 1:
            ans = 0
            for i in range(len(num)):
                ans += int(num[i])
            num = str(ans)
        return int(num)
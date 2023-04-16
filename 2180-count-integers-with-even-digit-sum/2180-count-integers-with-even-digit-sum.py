class Solution:
    def countEven(self, num: int) -> int:
        ans = 0
        for digits in range(1,num + 1):
            sub = 0 
            for digit in str(digits):
                sub += int(digit)
            if sub % 2 == 0:
                ans += 1
        return ans             
class Solution:
    def largestGoodInteger(self, num: str) -> str:
        digits = [str(i)*3 for i in range(9,-1,-1)]
        for digit in digits:
            if digit in num:
                return digit
        return ""
        
        
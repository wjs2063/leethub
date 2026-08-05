class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n <= 1 :
            return s
        ans = s[0]
        for i in range(n - 1):
            temp = s[i]
            for j in range(i + 1,n):
                temp += s[j]
                if temp == temp[::-1]:
                    if len(ans) < len(temp):
                        ans = temp
        return ans


        
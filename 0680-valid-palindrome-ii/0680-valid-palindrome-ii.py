class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        def palindrome(left,right,s,cnt):
            while left < right :
                if s[left] != s[right]:
                    if cnt == 1:
                        return 0
                    return palindrome(left,right - 1,s, cnt + 1) or palindrome(left + 1,right,s,cnt + 1) 
                left += 1
                right -= 1
            return 1
        return palindrome(0,len(s) - 1,s,0)
                
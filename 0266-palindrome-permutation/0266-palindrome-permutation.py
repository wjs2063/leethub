class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        from collections import Counter
        n = len(s)
        string_counter = Counter(s)
        even,odd = 0,0
        for k,v in string_counter.items():
            if v % 2 : odd +=1
            else: even += 1
        if n % 2 == 1:
            # middle 기준 양쪽 동일
            if odd == 1  :return True
        return odd == 0 
         
            
        
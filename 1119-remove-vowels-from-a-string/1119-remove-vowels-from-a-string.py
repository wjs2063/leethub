class Solution:
    def removeVowels(self, s: str) -> str:
        v = set()
        for ss in 'aeiou':
            v.add(ss)
        
        ans = ""
        for vv in s :
            if vv not in v :
                ans += vv
        return ans
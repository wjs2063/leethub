class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        ans = set()
        n = len(s)
        for BITMASK in range(2**n):
            sub = []
            # 1은 대문자, 0은 lower
            for idx in range(n):
                if s[idx].isalpha():
                    if BITMASK & (1 << idx):
                        sub.append(s[idx].upper())
                    else:
                        sub.append(s[idx].lower())
                else:
                    sub.append(s[idx])
            ans.add("".join(sub))
        return list(ans)
            
            
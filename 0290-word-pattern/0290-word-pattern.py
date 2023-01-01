from collections import defaultdict
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()
        if len(s) != len(pattern):
            return False
        h = defaultdict(lambda : "")
        for i in range(len(s)):
            # 등록이 안 되어있는 경우 등록
            if h[s[i]] == "":
                h[s[i]] = pattern[i]
            # 등록이 되어있는데 패턴이 같을수도있고 다를수도있음
            # 등록된 패턴이랑 다르면 
            elif h[s[i]] != pattern[i]:
                return False
        # 최종적으로 사용된 문자 개수가 같으면 ?
        return len(set(pattern)) == len(h.keys())
            
                
        
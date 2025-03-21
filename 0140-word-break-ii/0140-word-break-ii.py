class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        
        vis = set()
        q = deque([(0,"",tuple())])
        words = set(wordDict)
        n = len(s)
        ans = []
        while q :
            start,path,temp = q.popleft()
            if start >= n :
                ans.append(" ".join(temp))
                continue  
            for word in words:
                end = len(word)
                next_state = path + str(end)
                if s[start:start + end ] == word and next_state not in vis:
                    vis.add(next_state)
                    q.append((start + end,next_state,temp + (word,)))
        return ans


        
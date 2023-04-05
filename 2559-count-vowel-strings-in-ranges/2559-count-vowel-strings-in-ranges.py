class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        n = len(words)
        p = [0]*(n)
        vower = {"a","e","i","o","u"}
        for i,word in enumerate(words):
            if i >= 1:p[i] = p[i - 1]
            if word[0] in vower and word[-1] in vower:
                p[i] += 1
        p = [0] + p
        return [p[r + 1] - p[l] for l,r in queries]
                
                
            
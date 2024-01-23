class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        key_index = dict()
        
        for i,v in enumerate(keyboard):
            key_index[v] = i
        
        last = 0
        ans = 0
        for w in word:
            now = key_index[w]
            ans += abs(last - now)
            last = now
        return ans
        
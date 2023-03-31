from bisect import bisect_right
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        
        n = len(letters)
        
        idx = bisect_right(letters,target)
        if idx == n:
            return letters[0]
        return letters[idx]
        
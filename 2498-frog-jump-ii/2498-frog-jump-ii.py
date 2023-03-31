class Solution:
    def maxJump(self, stones: List[int]) -> int:
        
        ret = stones[1] - stones[0]
        
        for i in range(2,len(stones)):
            ret = max(ret,stones[i] - stones[i - 2])
        return ret
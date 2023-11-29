class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        flip_o = 0 
        flip_x = 0
        res = 0
        for i,v in enumerate(nums):
            if v == 1:
                flip_o += 1
                flip_x += 1
            else:
                # 현재 0 이라면 
                # flip 을 할수도있다
                flip_o = flip_x + 1
                flip_x = 0
            res = max(res,flip_o,flip_x)
        return res
                
                
            
                
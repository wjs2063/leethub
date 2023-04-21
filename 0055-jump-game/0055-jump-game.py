class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # nums[i] -> i 번째 인덱스에서 점프할수있는 최대 칸수 
        n = len(nums)
        last = 0
        for i,v in enumerate(nums):
            if last < i :return False
            last = max(last,i + v)
        return last >= n - 1
            
        
            
            
        
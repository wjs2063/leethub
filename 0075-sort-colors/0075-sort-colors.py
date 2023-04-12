class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        colors = [0]*3
        for i,v in enumerate(nums):
            colors[v] += 1
        ldx = 0
        for i in range(3):
            while colors[i]:
                nums[ldx] = i
                ldx += 1
                colors[i] -= 1
        
            
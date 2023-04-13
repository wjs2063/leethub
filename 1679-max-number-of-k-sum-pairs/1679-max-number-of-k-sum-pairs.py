class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        
        n = len(nums)
        nums.sort()
        
        l,r = 0,n - 1 
        ans = 0
        while l < r :
            target = nums[l] + nums[r]
            if target < k :
                l += 1
            elif target == k:
                ans += 1
                l += 1
                r -= 1
            else:
                r -= 1
        return ans
            
        

            
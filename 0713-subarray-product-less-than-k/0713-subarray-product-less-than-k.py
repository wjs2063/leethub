class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        from collections import defaultdict
        # 부분 배열의 곱이 k 미만 
        
        if k <= 1 :return 0
        
        ans = 0 
        
        product_val = 1 
        
        l = 0 
        for i,v in enumerate(nums):
            product_val *= v 
            
            
            while product_val >= k   :
                product_val //= nums[l]
                l += 1
            
            ans += i - l + 1
        return ans
            
class Solution:
    def countPairs(self, nums1: List[int], nums2: List[int]) -> int:
        # nums1[i] - nums2[i] - (nums1[j] - nums2[j] ) > 0 
        
        nums = sorted([x - y for x,y in zip(nums1,nums2)])
        ans = 0
        
        l,r = 0,len(nums) - 1
        
        while l < r :
            t = nums[l] + nums[r]
            
            if t > 0:
                ans += r - l
                r -= 1
            else:
                l += 1
        return ans
            
            
            
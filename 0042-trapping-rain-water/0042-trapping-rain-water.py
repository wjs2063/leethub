class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        l,r = 0,n - 1
        l_max,r_max = height[l],height[r]
        res = 0 
        while l <= r :
            l_max = max(l_max,height[l])
            r_max = max(r_max,height[r])
            res += l_max - height[l]
            res += r_max - height[r]
            if l_max <= r_max:
                l += 1
            else:
                r -= 1
        return res
            
            
        
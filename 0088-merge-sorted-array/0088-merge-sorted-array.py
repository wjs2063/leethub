class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = 0
        l = 0
        r = 0 
        res = [0] * (n + m)
        
        while l < m and r < n :
            if nums1[l] < nums2[r]:
                res[i] = nums1[l]
                l += 1
            else:
                res[i] = nums2[r]
                r += 1
            i += 1
        
        while l < m :
            res[i] = nums1[l]
            i += 1
            l += 1
        
        while r < n:
            res[i] = nums2[r]
            i += 1
            r += 1 
        for i,v in enumerate(res):
            nums1[i] = v
                
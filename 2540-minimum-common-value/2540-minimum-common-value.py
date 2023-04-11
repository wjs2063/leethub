class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        n1,n2 = set(nums1),set(nums2)
        nn = n1 & n2
        for n in sorted(nn) :
            return n
        return - 1
            
        
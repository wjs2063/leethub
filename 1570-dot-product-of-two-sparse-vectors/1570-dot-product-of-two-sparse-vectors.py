class SparseVector:
    def __init__(self, nums: List[int]):
        self.nums = nums
        

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        ans = 0
        for (v1,v2) in zip(self.nums,vec.nums):
            ans += v1 * v2
        return ans
        

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)
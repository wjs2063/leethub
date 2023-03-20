class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        l = [0] + nums
        r = nums + [0]
        for i in range(1,n + 1):
            l[i] += l[i - 1]
        for i in range(n - 1,-1,-1):
            r[i] += r[i + 1]
        print(l,r)
        for i,v in enumerate(nums):
            if l[i] == r[i + 1]:return i
        return -1
        
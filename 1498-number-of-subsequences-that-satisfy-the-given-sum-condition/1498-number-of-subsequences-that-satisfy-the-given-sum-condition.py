class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        n = len(nums)
        MOD = int(1e9 + 7)
        nums.sort()
        l,r = 0,n - 1
        res = 0
        while l <= r:
            if nums[l] + nums[r] <= target:
                # nums[l] 을 포함하는 sequence 
                # 2 3 4 5 일때 
                # (2,3),(2,4),(2,5)
                res = (res + (2 ** (r - l) )) % MOD
                l += 1
            else:
                r -= 1
        return res
            
        
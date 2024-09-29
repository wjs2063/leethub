class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        from collections import defaultdict
        # s[i:j] = i <= x < j -> sum 
        
        ans = 0 
        
        memo = defaultdict(int)
        """
        s[i:j] := s is divisible by k, then s - k is divisible by k 
                
        """
        p = 0 
        memo[0] = 1
        for i,v in enumerate(nums):

            ans += memo[(p % k + v % k - k) % k]
            memo[(p % k + v % k - k) % k] += 1
            p += v
        return ans
                
            
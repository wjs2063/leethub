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
            # 현재 스텝 이전까지의 누적합 p 
            # p의 mod,와 현재값 v 의 mod 의 합 p + v  
            ans += memo[(p + v ) % k]
            memo[(p + v ) % k] += 1
            p += v
        return ans
                
            
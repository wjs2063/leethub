class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        memo = {
            0 : 0,
            1: 0
        }
        # 좌측 인덱스
        l = 0
        ans = 0
        for r,v in enumerate(nums):
            # 현재 값의 개수를 증가시켜
            memo[v] += 1
            # 만약 0의 개수가 k 개 초과라면 좌측인덱스를 증가시켜 
            while memo[0] > k:
                memo[nums[l]] -= 1
                l += 1
            ans = max(ans,r - l  + 1)
        return ans
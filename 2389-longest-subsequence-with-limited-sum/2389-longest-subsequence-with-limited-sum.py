class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        from bisect import bisect_left,bisect_right
        n = len(nums)
        nums.sort()
        for i in range(1,n):
            nums[i] += nums[i - 1]
        ans = []
        for q in queries:
            idx = bisect_right(nums,q)
            ans.append(idx)
        return ans
                    
        
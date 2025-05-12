from collections import defaultdict
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        memo = defaultdict(int)
        for num in nums:
            memo[num] += 1
        for k,v in memo.items():
            if v >= n / 2 :
                return k 
        

        
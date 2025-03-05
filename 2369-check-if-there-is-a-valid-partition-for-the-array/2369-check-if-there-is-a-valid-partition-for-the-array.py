class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        # 같은 숫자가 2개,3개 이거나 1씩증가하는 수열이거나 
        # 주어진 수열을 위조건을 만족하는 모든 수열로 분할해야함 
        memo = {-1:True}
        def dp(i:int):
            if i in memo:
                return memo[i]
            flag = False
            # case 1 
            if i >= 1 and nums[i] == nums[i - 1]:
                # i - 2까지 True 라면 이번 케이스는 인정
                flag |= dp(i - 2)
            if i >= 2 and nums[i] == nums[i - 1] == nums[i - 2]:
                flag |= dp(i - 3)
            if i >= 2 and nums[i - 2] + 2 == nums[i - 1] + 1 == nums[i]:
                flag |= dp(i - 3)
            memo[i] = flag 
            return flag
        n = len(nums)
        return dp(n - 1)
             
        
class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        ans = 0
        for i in range(n - 2):
            j,k = i + 1,n - 1
            while j < k :
                if nums[i] + nums[j] + nums[k] >= target:
                    k -= 1
                else:
                    ans += (k - j ) 
                    
                    j += 1
                    
                    
        return ans
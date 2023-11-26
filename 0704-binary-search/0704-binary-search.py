class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # from bisect import bisect_left
        # idx = bisect_left(nums,target)
        # if idx < len(nums) and  nums[idx] == target:return idx
        # return -1
        sn,en = 0,len(nums) - 1
        
        while sn <= en :
            mid = (sn + en) // 2
            if nums[mid] > target:
                en = mid - 1
            elif nums[mid] < target:
                sn = mid + 1
            else:
                return mid 
        return -1
                
            
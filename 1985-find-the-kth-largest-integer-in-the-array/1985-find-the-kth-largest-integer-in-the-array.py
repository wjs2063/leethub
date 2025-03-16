class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        nums = list(map(int,nums))
        def merge_sort(nums) -> list :
            n = len(nums)

            if n <= 1 :
                return nums
            left = merge_sort(nums[:n // 2])
            right = merge_sort(nums[n // 2 :])

            temp = []
            l,r,k = 0,0,0

            # l 과 r 을 비교 
            while l < len(left) and r < len(right):
                if left[l] <= right[r]:
                    temp.append(left[l])
                    l += 1
                else:
                    temp.append(right[r])
                    r += 1
            
            while l < len(left):
                temp.append(left[l])
                l += 1
            while r < len(right):
                temp.append(right[r])
                r += 1
            return temp
        return str(merge_sort(nums)[-k])


        
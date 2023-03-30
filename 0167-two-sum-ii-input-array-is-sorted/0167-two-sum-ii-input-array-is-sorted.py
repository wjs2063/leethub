class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        l,r = 0, n - 1
        while l < r:
            sub = numbers[l] + numbers[r]
            
            if sub == target:
                return [l + 1,r + 1]
            
            if sub < target :
                l += 1
            else:
                r -= 1
                
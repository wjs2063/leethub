from collections import defaultdict
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        mini = min(nums)
        maxi = max(nums)
        
        table = defaultdict(int)
        
        for num in nums :
            table[num] += 1
            
        answer = []
        
        for index in range(mini,maxi + 1):
            answer += [index]*(table[index])
        return answer
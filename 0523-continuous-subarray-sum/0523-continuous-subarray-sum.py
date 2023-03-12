from collections import defaultdict
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        memo = defaultdict(lambda : int(1e6))
        flag = False
        n = len(nums)
        s = 0
        memo[0] = - 1
        for i in range(n):
            # 누적합계산을 해주는데
            s = (nums[i] + s ) % k
            # 2개이상이여야하니까 인덱스 차이가 2이상은 나야한다는소리
            # 즉 나머지가 같은것들을 찾아야한다 OK?
            # s 라는 값이 존재하면 
            if s in memo:
                if i - memo[s] > 1:
                    return True
            else:
                memo[s] = i
            
        return False
            
            
            
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        from collections import deque 

        q = deque([])
        res = int(-1e4)
        s = 0
        for idx,num in enumerate(nums):
            q.append(num)
            s += num
            if len(q) == k:
                res = max(res,s / k)
                s -= q.popleft()
        return res



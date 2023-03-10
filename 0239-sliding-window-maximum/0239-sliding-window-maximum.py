from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque([])
        # q 에는 인덱스를 넣어준다.
        ans = []
        for i,v in enumerate(nums):
            # 현재 값보다 작으면 다 버려
            while q and nums[q[-1]] < v:
                q.pop()
            
            q.append(i)
            
            if q[0] == i - k:
                q.popleft()
            
            if i >= k - 1:
                ans.append(nums[q[0]])
        return ans
                
                
        
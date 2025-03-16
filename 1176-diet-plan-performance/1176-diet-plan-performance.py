class Solution:
    def dietPlanPerformance(self, calories: List[int], k: int, lower: int, upper: int) -> int:
        from collections import deque
        calory_sum = 0

        n,l = len(calories),0
        q = deque([])
        res = 0
        point = 0
        while l < n :
            q.append(calories[l])
            res += calories[l]
            if len(q) == k :
                if res < lower:
                    point -= 1
                elif res > upper:
                    point += 1
                res -= q.popleft()
            l += 1
        return point
            

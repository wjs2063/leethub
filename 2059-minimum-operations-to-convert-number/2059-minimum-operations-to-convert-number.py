class Solution:
    def minimumOperations(self, nums: List[int], start: int, goal: int) -> int:
        from collections import deque
        
        def bfs(start,goal):
            seen = set()
            seen.add(start)
            q = deque([(start,0)])
            while q:
                x,time = q.popleft()
                if x == goal:return time
                
                for i,v in enumerate(nums):
                    if x + v == goal :return time + 1
                    if x - v == goal :return time + 1
                    if x ^ v == goal :return time + 1
                    if 0 <= x + v <= 1000 and  x + v not in seen:
                        
                        seen.add(x + v)
                        q.append((x + v,time + 1))
                    if 0 <= x - v <= 1000 and x - v not in seen:
                        
                        seen.add(x - v)
                        q.append((x - v,time + 1))
                    if 0 <=  x ^ v <= 1000 and x ^ v not in seen:
                        seen.add(x ^ v)
                        q.append((x ^ v,time + 1))
            return -1
        return bfs(start,goal)
            
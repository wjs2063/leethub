class Solution:
    def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:
        from collections import deque,defaultdict 

        counter = defaultdict(int)
        q = deque([])
        ans = []

        def find_x_th_smallest(counter,x) -> int:
            r = 0
            for key in range(-50,0):
                r += counter.get(key,0)
                if x <= r :
                    return key
            return 0



        for i,v in enumerate(nums):
            q.append(v)
            counter[v] += 1
            if len(q) == k:
                ans.append(find_x_th_smallest(counter,x))
                oldest = q.popleft()
                counter[oldest] -= 1
                if counter.get(oldest,0) == 0 :
                    counter.pop(oldest)
        return ans

        
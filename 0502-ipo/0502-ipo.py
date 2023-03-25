from heapq import heappush,heappop
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        # 현재 자본에서 선택할수있는 최고의 프로젝트를 선택한다.
        ans = 0
        n = len(profits)
        prj = list(zip(capital,profits))
        prj.sort()
        idx = 0
        h = []
        for _ in range(k):
            while idx < n and prj[idx][0] <= w:
                heappush(h,-prj[idx][1])
                idx += 1
            # 만족하는 것이없으면 불가능
            if len(h) == 0:
                break
            w += -heappop(h)
        return w
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        sub = []
        ans = []
        for x,y in points:
            sub.append([abs(x)**2 + abs(y)**2,x,y])
        sub.sort(key = lambda x:x[0])
        for i in range(k):
            ans.append(sub[i][1:])
        return ans
        
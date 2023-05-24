from heapq import heappush,heappop,heapify
class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        
        n = len(nums1)
        zz = list(zip(nums1,nums2))
        zz.sort(key = lambda x: -x[1])
        
        h = [z[0] for z in zz[:k]]
        
        s = sum(h)
        
        heapify(h)
        # 기본적으로 k - 1 개는 필수적으로 들어간다 -> k - 1번째부너 min 이 될수있다
        res = s * zz[k - 1][1]
        
        # 제일 작은거 하나빼고
        for i in range(k,n):
            s -= heappop(h)
            # 다음꺼 넣고 
            s += zz[i][0]
            heappush(h,zz[i][0])
            res = max(res,s * zz[i][1])
        return res
        
        
        
        
        
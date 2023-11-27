class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        
        # A1,A2,A3 
        # mink <= Ak <= maxk
        n = len(arrays)
        
        # 같은 array 에 포함되면안된다. 
        # global_min,max 중 1,2번쨰로 크고 작은것들을 모아서 계산해서 return 하자 
        
        global_min_arr = [(min(array),idx) for idx,array in enumerate(arrays)]
        global_max_arr = [(max(array),idx) for idx,array in enumerate(arrays)]
        
        global_min_arr.sort()
        global_max_arr.sort(reverse = True)
        
        (l1,l1x),(l2,l2x) = global_min_arr[0],global_min_arr[1]
        (m1,m1x),(m2,m2x) = global_max_arr[0],global_max_arr[1]
        # print(l1,l1x,l2,l2x)
        # print(m1,m1x,m2,m2x)
        if l1x != m1x:
            return abs(l1 - m1)
        return max(abs(m2 - l1),abs(m1 - l2))
        
        
        
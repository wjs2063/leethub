class Solution:
    def splitPainting(self, segments: List[List[int]]) -> List[List[int]]:
        
        from collections import defaultdict
        
        
        h = defaultdict(int)
        
        for l,r,c in segments:
            h[l] += c
            h[r] -= c 
        sn = 0
        ans = []
        for key in sorted(h):
            if h[sn]:
                ans.append([sn,key,h[sn]])
            h[key] += h[sn]
            sn = key
        return ans
                
            
        
from collections import Counter,defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        
        h = defaultdict(list)
        for key in c:
            h[c[key]].append(key)
        idx = 10**5
        ans = []
        while k:
            while k and h[idx] :
                
                ans.append(h[idx].pop())
                k -= 1
            idx -= 1
        return ans
                
                
                
            
        # Counting sort 
        
                
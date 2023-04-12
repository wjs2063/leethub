class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        
        items = [i for i in range(1,n + 1)]
        
        ans = []
        idx = 0
        for _,item in enumerate(items):
            if idx >= len(target):break
            ans.append("Push")
            if idx < len(target) and target[idx] != item:
                ans.append("Pop")
            else:
                idx += 1
        return ans
            
            
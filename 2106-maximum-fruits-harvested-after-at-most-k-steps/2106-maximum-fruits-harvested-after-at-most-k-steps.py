class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        n = 2*10**5 + 1
        left = [0]*(n)
        for x,y in fruits:
            left[x] += y
        for i in range(1,n):
            left[i] += left[i - 1]
        
        # 현재 기준으로 왼쪽 0,    오른쪽 k 
        # 현재 기준으로 왼쪽 1,    오른쪽 k - 1
        # 현재 기준으로 왼쪽 k - 1,오른쪽 1
        # 현재 기준으로 왼쪽 k    ,오른쪽 0 
        ans = 0
        for term in range(k + 1):
            l = max(0,startPos - term)
            r = max(startPos,startPos + k - 2*term)
            r = min(n - 1,r)
            if l == 0 :
                ans = max(ans,left[r])
            else:
                ans = max(ans,left[r] - left[l - 1])
        
        for term in range(k + 1):
            r = min(n - 1,startPos + term)
            l = min(startPos,startPos -(k - 2*term))
            l = max(0,l)
            if l == 0:
                ans = max(ans,left[r])
            else:
                ans = max(ans,left[r] - left[l - 1])

        return ans
            
        
        
        
            
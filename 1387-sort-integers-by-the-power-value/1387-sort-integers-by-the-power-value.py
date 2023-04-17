class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        from collections import defaultdict
        dp = defaultdict(int)
        
        def power(x):
            if x == 1: return 0
            if x not in dp:
                if x % 2 == 0 :
                    dp[x] = power(x // 2) + 1
                else:
                    dp[x] = power(3 * x + 1) + 1
            return dp[x]
        ans = []
        for x in range(lo,hi + 1):
            ans.append([x,power(x)])
        ans.sort(key = lambda x:(x[1],x[0]))
        return ans[k - 1][0]
                    
                
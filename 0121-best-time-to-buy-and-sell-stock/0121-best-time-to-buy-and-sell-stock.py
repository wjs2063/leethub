class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        r_max = 0
        res = 0
        for i in range(n - 1,-1,-1):
            r_max = max(r_max,prices[i])
            res = max(res,r_max - prices[i])
        return res
        
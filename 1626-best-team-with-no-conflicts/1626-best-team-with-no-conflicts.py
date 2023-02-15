class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        n = len(scores)
        xx = list(zip(scores,ages))
        xx.sort(key = lambda x:(x[1],x[0]))
        print(xx)
        dp = [0]*n
        for i in range(n):
            dp[i] = xx[i][0]
            for j in range(i):
                # i 보다 이전인 j 인덱스들에 대해서 
                if xx[j][0] <= xx[i][0]:
                    dp[i] = max(dp[i],dp[j] + xx[i][0])
        return max(dp)
                    
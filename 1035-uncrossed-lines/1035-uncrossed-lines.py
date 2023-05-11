class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        m = len(nums2)
        dp = [[0] * m for _ in range(n)]
        for i in range(m):
            dp[0][i] = 1 if nums1[0] == nums2[i] else 0
            if i >= 1:
                dp[0][i] = max(dp[0][i],dp[0][i - 1])
        for i in range(n):
            dp[i][0] = 1 if nums1[i] == nums2[0] else 0
            if i >= 1:
                dp[i][0] = max(dp[i][0],dp[i - 1][0])
        # dp[i][j] := nums1 의 i번째와 nums2의 j번째까지 진행했을떄 최댓값     
        for r in range(1,n):
            for c in range(1,m):
                if nums1[r] == nums2[c] :
                    dp[r][c] = max(dp[r - 1][c - 1] + 1,dp[r][c])
                else:
                    dp[r][c] = max(dp[r - 1][c],dp[r][c - 1],dp[r - 1][c - 1])
        return dp[-1][-1]
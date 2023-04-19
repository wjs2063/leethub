class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        from collections import defaultdict
        couple = defaultdict(lambda : - 1)
        n = len(row)
        for i in range(0,n,2):
            couple[i] = i + 1
            couple[i + 1] = i
        
        ans = 0
        
        for i in range(0,n,2):
            if couple[row[i]] != row[i + 1]:
                idx = row.index(couple[row[i]])
                row[i + 1],row[idx] = row[idx],row[i + 1]
                ans += 1
        return ans
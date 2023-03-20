class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        sub_set = dict()
        candidates.sort()
        def dfs(arr,idx,sub_sum,target):
            nonlocal ans,sub_set
            if arr in sub_set or sub_sum > target: return
            sub_set[arr] = 1
            if sub_sum == target :
                ans.append(list(arr))
                return
            for i in range(idx ,len(candidates)):
                dfs(arr + (candidates[i],),i + 1,sub_sum + candidates[i],target)
        dfs(tuple(),0,0,target)
        return ans
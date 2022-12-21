# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        # level wise 
        # level dict
        dp = defaultdict(list)
        def dfs(root,level):
            nonlocal dp
            if root == None:
                return
            dfs(root.left,level + 1)
            dfs(root.right,level + 1)
            dp[level].append(root.val)
        dfs(root,1)
        answer = []
        #
        for i in sorted(dp.keys()):
            answer.append(sum(dp[i])/len(dp[i]))
        return answer
            
                        

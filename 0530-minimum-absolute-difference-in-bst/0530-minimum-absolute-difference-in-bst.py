# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        ans = []
        
        def dfs(root):
            if not root:return
            nonlocal ans
            dfs(root.left)
            ans.append(root.val)
            dfs(root.right)
        dfs(root)
        n = len(ans)
        res = float("inf")
        for i in range(n - 1):
            res = min(res,ans[i + 1] - ans[i])
        return res
            
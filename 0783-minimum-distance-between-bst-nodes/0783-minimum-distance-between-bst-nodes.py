# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        ans = []
        def dfs(root):
            nonlocal ans
            if not root : return
            dfs(root.left)
            ans.append(root.val)
            dfs(root.right)
        dfs(root)
        res = int(1e10)
        for i in range(len(ans) - 1):
            res = min(res,ans[i + 1] - ans[i])
        return res
        
        
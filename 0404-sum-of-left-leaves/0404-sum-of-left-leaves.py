# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def dfs(root,past):
            if not root:return
            nonlocal ans
            if not root.left and not root.right and  past == "l":
                ans += root.val
            dfs(root.left,"l")
            dfs(root.right,"r")
        dfs(root,"")
        return ans
        
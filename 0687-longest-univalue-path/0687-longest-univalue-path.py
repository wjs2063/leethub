# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        
        res = 0
        def dfs(root):
            if not root :return 0
            nonlocal res
            l,r = dfs(root.left),dfs(root.right)
            left,right = 0,0
            if root.left and root.left.val == root.val:
                left = l + 1
            if root.right and root.right.val == root.val:
                right = r + 1
            res = max(res,left + right)
            return max(left,right)
        dfs(root)
        return res
            
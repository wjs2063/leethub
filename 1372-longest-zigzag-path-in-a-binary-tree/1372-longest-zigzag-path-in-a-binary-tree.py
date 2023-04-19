# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def dfs(root,cnt,past):
            # 0 -> left
            # 1 -> right 
            if not root: return
            nonlocal ans 
            if past > ans :
                ans = past
            if cnt % 2 == 0 :
                dfs(root.left,1 - cnt,past + 1)
                dfs(root.right,1 - cnt,0)
            else:
                dfs(root.right,1 - cnt,past + 1)
                dfs(root.left,1 - cnt,0)
        dfs(root,0,0)
        dfs(root,1,0)
        return ans
            
            
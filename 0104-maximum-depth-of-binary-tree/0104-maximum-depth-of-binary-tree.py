# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        answer  = 0 
        #
        def dfs(root,cnt):
            nonlocal answer
            if root == None:
                return
            answer = max(answer,cnt)
            dfs(root.left,cnt + 1)
            dfs(root.right,cnt + 1)
        dfs(root,1)
        return answer
            
            
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
        def dfs(root,c):
            if root == None :
                return
            nonlocal answer
            if root.left :
                dfs(root.left,c + 1)
            if root.right:
                dfs(root.right,c + 1)
            answer = max(answer,c)
        dfs(root,1)
        return answer
            
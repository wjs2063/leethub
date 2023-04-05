# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        res = 0
        
        def dfs(root,s):
            if root.left == None and root.right == None:
                nonlocal res
                res += int(s + str(root.val))
                return
            if root.left:
                dfs(root.left,s + str(root.val))
            if root.right:
                dfs(root.right,s + str(root.val))
        dfs(root,"")
        return res